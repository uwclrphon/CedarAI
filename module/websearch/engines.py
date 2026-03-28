import re
import time
import urllib.parse
import urllib.request
import urllib.error
import json
import html
from abc import ABC, abstractmethod
from typing import List, Optional

from .models import SearchResult, SearchResponse



_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


def _get(url: str, headers: Optional[dict] = None, timeout: int = 10) -> str:
    """简单 GET，返回 HTML 字符串"""
    req_headers = {"User-Agent": _DEFAULT_UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = "utf-8"
        ct = resp.headers.get_content_charset()
        if ct:
            charset = ct
        return resp.read().decode(charset, errors="replace")


def _strip_tags(text: str) -> str:
    """去除 HTML 标签"""
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()



class BaseEngine(ABC):
    name: str = "base"

    @abstractmethod
    def search(self, query: str, num: int = 10) -> List[SearchResult]:
        ...



class DuckDuckGoEngine(BaseEngine):
    """
    使用 DuckDuckGo HTML 接口（无需 API Key）
    """
    name = "DuckDuckGo"
    _URL = "https://html.duckduckgo.com/html/"

    def search(self, query: str, num: int = 10) -> List[SearchResult]:
        data = urllib.parse.urlencode({"q": query, "kl": "cn-zh"}).encode()
        req = urllib.request.Request(
            self._URL,
            data=data,
            headers={"User-Agent": _DEFAULT_UA, "Content-Type": "application/x-www-form-urlencoded"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")

        results = []
        blocks = re.findall(
            r'<div class="result[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>',
            body, re.S
        )
        for i, block in enumerate(blocks[:num]):
            m_title = re.search(r'<a[^>]+class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
            if not m_title:
                continue
            url = m_title.group(1)
            if url.startswith("//"):
                url = "https:" + url
            elif url.startswith("/"):
                qs = urllib.parse.parse_qs(urllib.parse.urlparse("https://x.com" + url).query)
                url = qs.get("uddg", [url])[0]

            title = _strip_tags(m_title.group(2))

            m_snip = re.search(r'class="result__snippet"[^>]*>(.*?)</a>', block, re.S)
            snippet = _strip_tags(m_snip.group(1)) if m_snip else ""

            results.append(SearchResult(
                title=title, url=url, snippet=snippet,
                source=self.name, rank=i + 1,
            ))
        return results



class BingEngine(BaseEngine):
    name = "Bing"
    _URL = "https://www.bing.com/search"

    def search(self, query: str, num: int = 10) -> List[SearchResult]:
        params = urllib.parse.urlencode({"q": query, "count": min(num, 50), "setlang": "zh-CHS"})
        body = _get(f"{self._URL}?{params}", headers={"Accept": "text/html"})

        results = []
        blocks = re.findall(r'<li class="b_algo"[^>]*>(.*?)</li>', body, re.S)
        for i, block in enumerate(blocks[:num]):
            m_title = re.search(r'<h2[^>]*><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
            if not m_title:
                continue
            url = m_title.group(1)
            title = _strip_tags(m_title.group(2))

            m_snip = re.search(r'<p[^>]*>(.*?)</p>', block, re.S)
            snippet = _strip_tags(m_snip.group(1)) if m_snip else ""

            m_date = re.search(r'<span class="news_dt">(.*?)</span>', block)
            date = m_date.group(1).strip() if m_date else None

            results.append(SearchResult(
                title=title, url=url, snippet=snippet,
                source=self.name, rank=i + 1, published_date=date,
            ))
        return results



class GoogleEngine(BaseEngine):
    name = "Google"
    _URL = "https://www.google.com/search"

    def search(self, query: str, num: int = 10) -> List[SearchResult]:
        params = urllib.parse.urlencode({"q": query, "num": min(num, 20), "hl": "zh-CN"})
        body = _get(f"{self._URL}?{params}")

        results = []
        blocks = re.findall(r'<div class="g"[^>]*>(.*?)</div>\s*</div>\s*</div>', body, re.S)
        for i, block in enumerate(blocks[:num]):
            m_link = re.search(r'<a href="(/url\?[^"]+|https?://[^"]+)"', block)
            if not m_link:
                continue
            raw_url = m_link.group(1)
            if raw_url.startswith("/url?"):
                qs = urllib.parse.parse_qs(urllib.parse.urlparse("https://g.com" + raw_url).query)
                url = qs.get("q", [raw_url])[0]
            else:
                url = raw_url

            m_title = re.search(r'<h3[^>]*>(.*?)</h3>', block, re.S)
            title = _strip_tags(m_title.group(1)) if m_title else url

            m_snip = re.search(r'<div[^>]+data-sncf[^>]*>(.*?)</div>', block, re.S)
            if not m_snip:
                m_snip = re.search(r'<span[^>]+>([\u4e00-\u9fffA-Za-z][^<]{20,})</span>', block, re.S)
            snippet = _strip_tags(m_snip.group(1)) if m_snip else ""

            results.append(SearchResult(
                title=title, url=url, snippet=snippet,
                source=self.name, rank=i + 1,
            ))
        return results



class SearXNGEngine(BaseEngine):
    """
    连接自托管的 SearXNG 实例（JSON API）
    用法: SearXNGEngine(base_url="https://your-searxng.example.com")
    """
    name = "SearXNG"

    def __init__(self, base_url: str = "https://searx.be"):
        self.base_url = base_url.rstrip("/")

    def search(self, query: str, num: int = 10) -> List[SearchResult]:
        params = urllib.parse.urlencode({
            "q": query, "format": "json",
            "categories": "general", "language": "zh-CN",
        })
        body = _get(f"{self.base_url}/search?{params}")
        data = json.loads(body)

        results = []
        for i, item in enumerate(data.get("results", [])[:num]):
            results.append(SearchResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                snippet=item.get("content", ""),
                source=self.name,
                rank=i + 1,
                published_date=item.get("publishedDate"),
            ))
        return results



ENGINES = {
    "duckduckgo": DuckDuckGoEngine,
    "bing": BingEngine,
    "google": GoogleEngine,
    "searxng": SearXNGEngine,
}
