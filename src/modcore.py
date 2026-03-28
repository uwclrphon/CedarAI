import abc

class ModCore(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def register_mod(self):
        pass
class ModTools(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def register_tools(self):
        pass
    @abc.abstractmethod
    def run_tools(self):
        pass