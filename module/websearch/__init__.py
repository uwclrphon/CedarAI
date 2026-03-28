"""
websearch —— 轻量级 Python 网络搜索库
======================================

支持 DuckDuckGo、Bing、Google、SearXNG，无需 API Key。

基本用法::

    from websearch import WebSearch

    ws = WebSearch()                        # 默认使用 DuckDuckGo
    resp = ws.search("Python 异步编程")
    print(resp)                             # 格式化输出

    # 遍历结果
    for r in resp:
        print(r.rank, r.title)
        print(r.url)
        print(r.snippet)

    # 指定引擎 + 备用引擎
    ws = WebSearch(engine="bing", fallback=["duckduckgo"])
    resp = ws.search("人工智能最新进展", num=5)

    # 一行快捷搜索
    resp = WebSearch.quick("今日新闻", num=3)

    # 返回字典（方便 JSON 序列化）
    data = ws.search_json("量子计算")

    # 查看所有可用引擎
    print(WebSearch.available_engines())
"""

from .client import WebSearch
from .models import SearchResult, SearchResponse
from .engines import (
    DuckDuckGoEngine,
    BingEngine,
    GoogleEngine,
    SearXNGEngine,
    ENGINES,
)

__all__ = [
    "WebSearch",
    "SearchResult",
    "SearchResponse",
    "DuckDuckGoEngine",
    "BingEngine",
    "GoogleEngine",
    "SearXNGEngine",
    "ENGINES",
]

__version__ = "1.0.0"
__author__ = "websearch"
