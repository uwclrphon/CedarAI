from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class SearchResult:
    """单条搜索结果"""
    title: str
    url: str
    snippet: str
    source: str = ""
    published_date: Optional[str] = None
    rank: int = 0

    def __str__(self):
        lines = [
            f"[{self.rank}] {self.title}",
            f"    URL: {self.url}",
            f"    {self.snippet}",
        ]
        if self.published_date:
            lines.append(f"    日期: {self.published_date}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "rank": self.rank,
            "title": self.title,
            "url": self.url,
            "snippet": self.snippet,
            "source": self.source,
            "published_date": self.published_date,
        }


@dataclass
class SearchResponse:
    """搜索响应，包含多条结果"""
    query: str
    results: List[SearchResult] = field(default_factory=list)
    total_found: int = 0
    engine: str = ""
    elapsed_seconds: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def __str__(self):
        header = (
            f"🔍 查询: {self.query}\n"
            f"   引擎: {self.engine} | 结果数: {len(self.results)} | "
            f"耗时: {self.elapsed_seconds:.2f}s\n"
            f"{'─' * 60}"
        )
        body = "\n\n".join(str(r) for r in self.results)
        return f"{header}\n\n{body}" if body else f"{header}\n\n（无结果）"

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "engine": self.engine,
            "total_found": self.total_found,
            "elapsed_seconds": self.elapsed_seconds,
            "timestamp": self.timestamp,
            "results": [r.to_dict() for r in self.results],
        }

    def __len__(self):
        return len(self.results)

    def __iter__(self):
        return iter(self.results)

    def __getitem__(self, idx):
        return self.results[idx]
