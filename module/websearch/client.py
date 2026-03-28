"""
WebSearch 主客户端
"""
import time
from typing import List, Optional, Union

from .models import SearchResult, SearchResponse
from .engines import BaseEngine, DuckDuckGoEngine, BingEngine, GoogleEngine, SearXNGEngine, ENGINES


class WebSearch:
    """
    网络搜索客户端，支持多引擎、自动故障转移。

    快速开始::

        from websearch import WebSearch

        ws = WebSearch()
        resp = ws.search("Python 异步编程")
        print(resp)

        # 只要结果列表
        for r in resp:
            print(r.title, r.url)

    参数
    ----
    engine : str | BaseEngine
        搜索引擎名称（"duckduckgo"、"bing"、"google"、"searxng"）
        或自定义引擎实例。默认 "duckduckgo"。
    fallback : list[str]
        当主引擎失败时依次尝试的备用引擎列表。
    timeout : int
        网络请求超时秒数（默认 15）。
    proxy : str | None
        HTTP/HTTPS 代理地址，例如 "http://127.0.0.1:7890"。
    """

    def __init__(
        self,
        engine: Union[str, BaseEngine] = "duckduckgo",
        fallback: Optional[List[str]] = None,
        timeout: int = 15,
        proxy: Optional[str] = None,
    ):
        self._engine = self._resolve_engine(engine)
        self._fallback = [self._resolve_engine(e) for e in (fallback or [])]
        self.timeout = timeout

        if proxy:
            import urllib.request as _ur
            _ur.install_opener(
                _ur.build_opener(
                    _ur.ProxyHandler({"http": proxy, "https": proxy})
                )
            )


    @staticmethod
    def _resolve_engine(engine: Union[str, BaseEngine]) -> BaseEngine:
        if isinstance(engine, BaseEngine):
            return engine
        key = engine.lower()
        if key not in ENGINES:
            raise ValueError(
                f"未知引擎 '{engine}'，可选: {list(ENGINES.keys())}"
            )
        return ENGINES[key]()

    def _run_engine(self, engine: BaseEngine, query: str, num: int) -> List[SearchResult]:
        return engine.search(query, num)


    def search(
        self,
        query: str,
        num: int = 10,
    ) -> SearchResponse:
        """
        执行搜索，返回 SearchResponse 对象。

        参数
        ----
        query : str
            搜索关键词或问题。
        num : int
            期望返回的结果数量（默认 10）。

        返回
        ----
        SearchResponse
        """
        if not query or not query.strip():
            raise ValueError("查询内容不能为空")

        engines_to_try = [self._engine] + self._fallback
        last_error = None

        for engine in engines_to_try:
            try:
                t0 = time.perf_counter()
                results = self._run_engine(engine, query.strip(), num)
                elapsed = time.perf_counter() - t0

                return SearchResponse(
                    query=query,
                    results=results,
                    total_found=len(results),
                    engine=engine.name,
                    elapsed_seconds=round(elapsed, 3),
                )
            except Exception as e:
                last_error = e
                continue

        # 所有引擎都失败
        raise RuntimeError(
            f"所有搜索引擎均失败。最后一次错误: {last_error}"
        ) from last_error

    def search_text(self, query: str, num: int = 10) -> str:
        """返回格式化的纯文本结果（直接 print 用）"""
        return str(self.search(query, num))

    def search_json(self, query: str, num: int = 10) -> dict:
        """返回字典格式结果（适合 JSON 序列化）"""
        return self.search(query, num).to_dict()

    @classmethod
    def quick(cls, query: str, num: int = 10, engine: str = "duckduckgo") -> SearchResponse:
        """一行代码搜索::

            resp = WebSearch.quick("今日新闻")
        """
        return cls(engine=engine).search(query, num)


    @staticmethod
    def available_engines() -> List[str]:
        """返回所有可用的引擎名称列表"""
        return list(ENGINES.keys())

    def use_engine(self, engine: Union[str, BaseEngine]) -> "WebSearch":
        """切换搜索引擎，返回 self 以支持链式调用"""
        self._engine = self._resolve_engine(engine)
        return self

    def __repr__(self):
        return f"WebSearch(engine={self._engine.name!r})"
