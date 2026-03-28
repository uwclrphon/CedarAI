from src.modcore import *
#示例mod
class Aifr(ModTools):
    def __init__(self):
        pass
    def run_tools(self):
        return 330
    def register_tools(self):
        return """Aifr():获取埃菲尔铁塔的高度"""

class FileAndRun(ModCore):
    def __init__(self):
        pass
    def register_mod(self):
        return [Aifr()]
    