import openai

# 基础配置（SiliconFlow 平台）
BASE_URL = "http://47.111.92.240/v1"  # 必须带/v1后缀
API_KEY = "sk-1oPk1eZqWKSPmGzbx5f5c4M6ktNWajqiwjhLD8zRkDvAu0ab"
MODEL_NAME = "gpt-4-turbo"  # 千问3.5模型

class AiModel:
    def __init__(self, api_url, api_key, model_name, system_prompt):
        self.api_url = api_url
        self.api_key = api_key
        self.model_name = model_name
        self.system_prompt = system_prompt
        
        # 核心：初始化对话历史（包含系统指令，作为上下文基础）
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def get_response(self, prompt):
        """
        获取AI回复，自动记录对话历史
        :param prompt: 本次用户提问内容
        :return: AI回复内容
        """
        try:
            # 1. 将本次用户提问追加到对话历史
            self.conversation_history.append({"role": "user", "content": prompt})
            
            # 2. 初始化客户端并调用API（传入完整对话历史）
            client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.api_url
            )
            response = client.chat.completions.create(
                model=self.model_name,
                messages=self.conversation_history,  # 传入完整上下文
                temperature=0.0,
                max_tokens=500
            )
            
            # 3. 提取AI回复，并追加到对话历史
            ai_reply = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": ai_reply})
            
            return ai_reply
        
        except Exception as e:
            return f"调用失败：{str(e)}"
    
    def clear_history(self):
        """清空对话历史（仅保留系统指令），可选功能"""
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def get_history(self):
        """获取当前对话历史，用于调试/查看"""
        return self.conversation_history

if __name__ == '__main__':
    # 实例化AI模型
    ai_model = AiModel(
        api_url=BASE_URL,
        api_key=API_KEY,
        model_name=MODEL_NAME,
        system_prompt='现在是windows系统，你以后我提问题，你要输出一段指令，格式{mes:"操作描述",cmd:["命令1","命令2"]}不要添加多余内容，直接输出这个格式'
    )
    
    # 测试多轮对话（验证记忆功能）
    prompt1 = "请帮我新建文件text.txt"
    response1 = ai_model.get_response(prompt1)
    print("第一轮回复：", response1)
    print("-" * 50)
    
    prompt2 = "把刚才的文件名改成test.txt"  # 引用上一轮的内容
    response2 = ai_model.get_response(prompt2)
    print("第二轮回复：", response2)
    print("-" * 50)
    
    # 可选：查看完整对话历史
    print("对话历史：")
    for msg in ai_model.get_history():
        print(f"{msg['role']}: {msg['content']}")
    
    # 可选：清空历史
    # ai_model.clear_history()