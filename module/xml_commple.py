import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import json
import re
from typing import *
# 新增：导入 escape 函数用于转义特殊字符
from xml.sax.saxutils import escape

class XML_Commple:
    def __init__(self, xml_text):
        # 1. 预处理：去除不可见控制字符
        illegal_chars = r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]'
        clean_text = re.sub(illegal_chars, '', xml_text)

        # 2. 关键修复：转义 XML 特殊字符
        # 这会将 < 转义为 < > 转义为 > " 转义为 " 等
        # 注意：我们不能直接转义整个字符串，因为那样会把 <action> 标签也转义了。
        # 正确的做法是只转义标签内部的内容，但正则提取比较复杂。
        # 这里采用一个折中方案：利用 XML 解析器的容错性或者手动替换。
        
        # 方案 A (推荐): 手动替换常见的 C++ 代码冲突字符
        # 将 <iostream> 等替换为 <iostream>
        # 注意：这只是一个简单的补丁，如果代码中包含 ]] 等CDATA序列结束符仍可能出错
        
        # 为了更稳健，我们构建一个新的 XML 字符串，确保内容被转义
        # 但由于我们不知道哪里是标签哪里是内容，这里使用一个简单的正则替换
        # 将所有不在标签尖括号内的 < 和 > 进行转义
        
        # 简单粗暴的修复：将所有 < 替换为 < (除了开头的标签)
        # 注意：这假设输入格式比较规范
        
        # 更好的方法：使用正则表达式找到标签内的内容并转义
        def replace_content(match):
            # group(1) 是标签名，group(2) 是内容
            tag = match.group(1)
            content = match.group(2)
            # 转义内容中的特殊字符
            escaped_content = escape(content)
            return f"<{tag}>{escaped_content}</{tag}>"

        # 正则匹配 <tag>content</tag> 结构
        # 这里的正则假设标签没有属性，且内容不包含嵌套标签
        pattern = re.compile(r"<(\w+)>(.*?)</\1>", re.DOTALL)
        
        # 执行替换
        safe_text = pattern.sub(replace_content, clean_text)
        
        # 3. 包装在 <root> 中
        self.xml_text = f"<root>{safe_text}</root>"
        
        # 4. 解析
        self.root = ET.fromstring(self.xml_text)
        
        self.data: Dict[str, str] = {}
        for child in self.root:
            self.data[child.tag] = child.text
            
        for key, value in self.data.items():
            try:
                self.data[key] = json.loads(value)
            except:
                pass

    def get_data(self) -> Dict[str, Union[Union[str,list], Dict]]:
        return self.data

# Writer 类保持不变
class XML_Commple_Writer:
    # ... (保持原样) ...
    def __init__(self, data: Dict[str, Union[str, list, Dict]]):
        self.data = data
        self.root = Element('root')
        for key, value in data.items():
            if isinstance(value, str):
                child = Element(key)
                child.text = value
                self.root.append(child)
            elif isinstance(value, list) or isinstance(value, dict):
                child = Element(key)
                child.text = json.dumps(value)
                self.root.append(child)

    def get_xml_text(self) -> str:
        return ET.tostring(self.root, encoding='unicode')
