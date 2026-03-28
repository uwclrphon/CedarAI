from module import Ai_api
from module import system_prompt
from module import xml_commple
from src.modcore import *
from module.websearch import WebSearch
from typing import *
import importlib.util
import os
import platform
import subprocess
import ast
import shutil
import psutil
import requests
import json
from datetime import datetime

def ReadFile(file_path):
    if not os.path.exists(file_path):
        return "Error: 文件不存在"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: 读取文件失败 ({e})"

def WriteToFile(file_path, content):
    try:
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        with open(file_path, 'w', encoding='utf-8') as f: 
            # 修复编码问题：直接写入内容，不进行额外的编码/解码
            f.write(content)
        return "写入成功"
    except Exception as e:
        return f"Error: 写入文件失败 ({e})"

def GetDirectoryPath(a=0):
    return os.getcwd()

def GetSystemInformation(a=0):
    system_name = platform.system()
    cpu_info = platform.processor()
    
    mem = psutil.virtual_memory()
    memory_size = f"{mem.total / (1024**3):.2f} GB"
    
    disk = psutil.disk_usage('/')
    if system_name == 'Windows':
        disk = psutil.disk_usage('C:\\')
    disk_size = f"{disk.total / (1024**3):.2f} GB"
    gpu_manufacturer = "Unknown"
    gpu_model = "Unknown"
    
    return {
        "type": system_name,
        "CPUManufacturer": "Unknown", 
        "CPUModel": cpu_info,
        "GPUManufacturer": gpu_manufacturer,
        "GPUModel": gpu_model,
        "MemorySize": memory_size,
        "DiskSize": disk_size
    }

def RunCommand(command):
    try:
        encoding = 'gbk' if platform.system() == 'Windows' else 'utf-8'
        
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding=encoding,
            errors='replace' 
        )
        
        output = ""
        for line in process.stdout:
            print(line, end='')
            output += line
            
        process.wait()
        return output
    except Exception as e:
        return f"Error: 命令执行失败 ({e})"

def ListDir(dir):
    try:
        list_dir = []
        for file in os.listdir(dir):
            full_path = os.path.join(dir, file)
            if os.path.isfile(full_path):
                list_dir.append({"name": file, "type": "file"})
            else:
                list_dir.append({"name": file, "type": "dir"})
        return list_dir
    except Exception as e:
        return f"Error: 列出目录失败 ({e})"

def InternetSearch(text):
    ws = WebSearch()
    data = ws.search_json(text)
    output = []
    for i in data["results"]:
        output.append(i["snippet"])
    return output

def CreateDir(dir_path):
    """创建文件夹"""
    try:
        if os.path.exists(dir_path):
            return "Error: 文件夹已存在"
        os.makedirs(dir_path)
        return "创建成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 创建文件夹失败 ({e})"

def RemoveFile(file_path):
    """删除文件"""
    try:
        if not os.path.exists(file_path):
            return "Error: 文件不存在"
        os.remove(file_path)
        return "删除成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 删除文件失败 ({e})"

def RemoveDir(dir_path):
    """删除文件夹"""
    try:
        if not os.path.exists(dir_path):
            return "Error: 文件夹不存在"
        shutil.rmtree(dir_path)
        return "删除成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 删除文件夹失败 ({e})"

def RenameFile(old_file_path, new_file_path):
    """重命名文件"""
    try:
        if not os.path.exists(old_file_path):
            return "Error: 文件不存在"
        if os.path.exists(new_file_path):
            return "Error: 新文件名已存在"
        os.rename(old_file_path, new_file_path)
        return "重命名成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 重命名文件失败 ({e})"

def RenameDir(old_dir_path, new_dir_path):
    """重命名文件夹"""
    try:
        if not os.path.exists(old_dir_path):
            return "Error: 文件夹不存在"
        if os.path.exists(new_dir_path):
            return "Error: 新文件夹名已存在"
        os.rename(old_dir_path, new_dir_path)
        return "重命名成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 重命名文件夹失败 ({e})"

def CopyFile(old_file_path, new_file_path):
    """复制文件"""
    try:
        if not os.path.exists(old_file_path):
            return "Error: 文件不存在"
        if os.path.exists(new_file_path):
            return "Error: 新文件名已存在"
        dir_name = os.path.dirname(new_file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        shutil.copy2(old_file_path, new_file_path)
        return "复制成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 复制文件失败 ({e})"

def CopyDir(old_dir_path, new_dir_path):
    """复制文件夹"""
    try:
        if not os.path.exists(old_dir_path):
            return "Error: 文件夹不存在"
        if os.path.exists(new_dir_path):
            return "Error: 新文件夹名已存在"
        dir_name = os.path.dirname(new_dir_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        shutil.copytree(old_dir_path, new_dir_path)
        return "复制成功"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 复制文件夹失败 ({e})"

def DownloadFile(url, save_path):
    """下载文件"""
    try:
        if os.path.exists(save_path):
            return "Error: 文件已存在"
        
        dir_name = os.path.dirname(save_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return "下载成功"
    except requests.exceptions.RequestException:
        return "Error: 网络错误或URL无效"
    except PermissionError:
        return "Error: 没有权限"
    except Exception as e:
        return f"Error: 下载文件失败 ({e})"

def load_mods():
    """
    扫描 mods 文件夹，读取/更新 config.json，根据配置动态加载 Mod。
    返回: (tools_dict, tools_description_list)
    """
    tools = {}
    tool_descriptions = []
    mods_dir = "mods"
    config_path = "modsconfig.json"
    
    mod_config = {}
    config_changed = False
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                mod_config = config_data.get("mods", {})
        except Exception as e:
            print(f"警告: 读取配置文件失败 ({e})，将重置配置。")
            mod_config = {}
    else:
        print(f"提示: 未找到配置文件 {config_path}，将创建新配置。")

    if not os.path.exists(mods_dir):
        if not os.path.exists(config_path):
            try:
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump({"mods": {}}, f, indent=4, ensure_ascii=False)
            except:
                pass
        return tools, tool_descriptions

    print(f"正在扫描 {mods_dir} ...")
    
    for filename in os.listdir(mods_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            mod_name = filename[:-3]
            
            if mod_name not in mod_config:
                print(f"发现新 Mod: {mod_name}，已添加到配置 (默认启用)")
                mod_config[mod_name] = {"enabled": True}
                config_changed = True
            
            is_enabled = mod_config[mod_name].get("enabled", True)
            
            if not is_enabled:
                print(f"跳过 Mod: {mod_name} (已在配置中禁用)")
                continue

            file_path = os.path.join(mods_dir, filename)
            print(f"正在加载 Mod: {mod_name} ...")
            
            try:
                spec = importlib.util.spec_from_file_location(mod_name, file_path)
                mod_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod_module)
                
                for item_name in dir(mod_module):
                    item = getattr(mod_module, item_name)
                    if isinstance(item, type) and issubclass(item, ModCore) and item != ModCore:
                        mod_instance = item()
                        mod_tools_list = mod_instance.register_mod()
                        
                        for tool in mod_tools_list:
                            tool_name = tool.__class__.__name__
                            tools[tool_name] = tool.run_tools
                            desc = tool.register_tools()
                            tool_descriptions.append(desc)
                            print(f"  - 注册工具: {tool_name}")
                            
            except Exception as e:
                print(f"❌ 加载 {mod_name} 失败: {e}")

    if config_changed:
        print("配置文件已更新，正在保存...")
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump({"mods": mod_config}, f, indent=4, ensure_ascii=False)
            print("配置文件保存成功。")
        except Exception as e:
            print(f"❌ 保存配置文件失败: {e}")
                
    return tools, tool_descriptions



class ReActAgent:
    def __init__(self, tools: Dict[str, Callable], model: str = Ai_api.MODEL_NAME, api_key: str = Ai_api.API_KEY, base_url: str = Ai_api.BASE_URL, system_prompt_content: str = system_prompt.react):
        self.tools = tools
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        self.ai_model = Ai_api.AiModel(self.base_url, self.api_key, self.model, system_prompt_content)

    def parse_action_args(self, action_str: str):
        """
        安全解析 Action 参数。
        例如: WriteToFile("path", "content") -> ["path", "content"]
        """
        try:
            args_str = action_str.split('(', 1)[1].rsplit(')', 1)[0]
        except IndexError:
            return []
        if '\\n' in args_str or '\n' in args_str:
            parts = args_str.split(',', 1)
            parsed = []
            for p in parts:
                p = p.strip()
                if (p.startswith('"') and p.endswith('"')) or (p.startswith("'") and p.endswith("'")):
                    parsed.append(p[1:-1].encode('utf-8').decode('unicode_escape'))
                else:
                    parsed.append(p)
            return parsed
        else:
            try:
                return list(ast.literal_eval(f'[{args_str}]'))
            except:
                return [a.strip().strip('\'').strip('\"') for a in args_str.split(',')]

    def run(self, user_input: str, line_list=[]) -> str:
        user_message_html = f'''
        <div class="message user-message">
            <div class="message-header">
                <span class="message-sender">用户</span>
                <span class="message-time">{datetime.now().strftime("%H:%M")}</span>
            </div>
            <div class="message-content">
                {user_input}
            </div>
        </div>
        '''
        line_list.append(user_message_html)
        
        user_input = xml_commple.XML_Commple_Writer({"task": user_input}).get_xml_text()
        
        while True:
            try:
                content = self.ai_model.get_response(user_input)
                print("----------------------")
                print(content)
                xml = xml_commple.XML_Commple(content)
                xml_data = xml.get_data()
                
                if 'thought' in xml_data:
                    print(f'Thought: {xml_data["thought"]}')
                    thought_html = f'''
                    <div class="message ai-message thought-message">
                        <div class="message-header">
                            <span class="message-sender">AI思考</span>
                            <span class="message-time">{datetime.now().strftime("%H:%M")}</span>
                        </div>
                        <div class="message-content">
                            {xml_data['thought']}
                        </div>
                    </div>
                    '''
                    line_list.append(thought_html)
                
                if 'final_answer' in xml_data:
                    final_answer = xml_data['final_answer']
                    print(f'Final Answer: {final_answer}')
                    final_answer_html = f'''
                    <div class="message ai-message final-answer">
                        <div class="message-header">
                            <span class="message-sender">AI回答</span>
                            <span class="message-time">{datetime.now().strftime("%H:%M")}</span>
                        </div>
                        <div class="message-content">
                            {final_answer}
                        </div>
                    </div>
                    '''
                    line_list.append(final_answer_html)
                    return final_answer
                
                if 'action' not in xml_data:
                    print("Error: XML 中未找到 action 标签")
                    user_input = xml_commple.XML_Commple_Writer({"observation": "Error: 缺少 action 标签"}).get_xml_text()
                    continue

                action = xml_data['action']
                print(f'Raw Action: {action}')
                
                action_name = action.split('(')[0]
                action_args = self.parse_action_args(action)
                
                if action_name not in self.tools:
                    error_msg = f"Error: 未知工具 '{action_name}'"
                    print(error_msg)
                    user_input = xml_commple.XML_Commple_Writer({"observation": error_msg}).get_xml_text()
                    continue

                action_return = self.tools[action_name](*action_args)
                print(f'Action: {action_name}({action_args}) -> {action_return}')
                action_html = f'''
                <div class="message ai-message action-message">
                    <div class="message-header">
                        <span class="message-sender">AI动作</span>
                        <span class="message-time">{datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <div class="message-content">
                        执行动作：{action_name}({action_args}) -> {action_return}
                    </div>
                </div>
                '''
                line_list.append(action_html)
                observation = {"observation": action_return}
                observation_xml_text = xml_commple.XML_Commple_Writer(observation).get_xml_text()
                user_input = observation_xml_text
            except Exception as e:
                print(f"Agent 运行出错: {e}")
                error_html = f'''
                <div class="message error-message">
                    <div class="message-header">
                        <span class="message-sender">错误</span>
                        <span class="message-time">{datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <div class="message-content">
                        {str(e)}
                    </div>
                </div>
                '''
                line_list.append(error_html)
                user_input = xml_commple.XML_Commple_Writer({"observation": f"Error: {str(e)}"}).get_xml_text()

def init_agent(model=Ai_api.MODEL_NAME, api_key=Ai_api.API_KEY, base_url=Ai_api.BASE_URL):

    mod_tools, mod_descs = load_mods()
    
    base_tools = {
        "ReadFile": ReadFile,
        "WriteToFile": WriteToFile,
        "GetDirectoryPath": GetDirectoryPath,
        "GetSystemInformation": GetSystemInformation,
        "RunCommand": RunCommand,
        "ListDir": ListDir,
        "InternetSearch": InternetSearch,
        "CreateDir": CreateDir,
        "RemoveFile": RemoveFile,
        "RemoveDir": RemoveDir,
        "RenameFile": RenameFile,
        "RenameDir": RenameDir,
        "CopyFile": CopyFile,
        "CopyDir": CopyDir,
        "DownloadFile": DownloadFile
    }
    
    all_tools = {**base_tools, **mod_tools}
    
    if mod_descs:
        extended_react = system_prompt.react + "\n社区Mod工具:\n" + "\n".join(mod_descs)
    else:
        extended_react = system_prompt.react

    agent = ReActAgent(tools=all_tools, system_prompt_content=extended_react, model=model, api_key=api_key, base_url=base_url)
    
    return agent

if __name__ == '__main__':
    agent = init_agent()
    while True:
        user_input = input("请输入你的指令: ")
        result = agent.run(user_input)