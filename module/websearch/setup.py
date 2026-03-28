from setuptools import setup, find_packages

setup(
    name="websearch",
    version="1.0.0",
    description="轻量级 Python 网络搜索库，支持 DuckDuckGo、Bing、Google、SearXNG",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],          # 仅用标准库，零依赖
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
