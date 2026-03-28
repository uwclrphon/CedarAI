# CedarAI - 智能桌面AI助手

CedarAI 是一个基于 Python 和 PySide6 开发的桌面AI助手应用程序，采用 ReAct（Reasoning-Acting）架构，支持多种AI模型API，具备文件操作、网络搜索、模块扩展等强大功能。


## ✨ 功能特性

### 🤖 多模型支持
- **OpenAI** (GPT系列)
- **Google Gemini**
- **DeepSeek**
- **Anthropic Claude**
- **SiliconFlow**
- **月之暗面 (Moonshot)**
- **阿里通义千问 (Qwen)**
- **自定义API** (支持任何兼容OpenAI API的接口)

### 🛠️ 核心能力
- **ReAct代理架构**：思考-行动循环，实现复杂任务分解
- **文件系统操作**：创建、删除、重命名、复制文件和文件夹
- **网络搜索**：集成多搜索引擎，支持故障转移
- **模块系统**：可扩展的插件架构，动态加载功能模块
- **美观界面**：现代化UI设计，透明窗口，阴影效果
- **实时聊天**：支持多轮对话，消息分类显示

### 🎨 界面特色
- 无边框透明窗口设计
- 消息分类显示（用户、AI、思考、动作、最终答案、错误）
- 响应式布局，美观的CSS样式
- 设置向导，简化配置过程

## 🚀 快速开始

### 环境要求
- Python 3.8+
- Windows/Linux/macOS

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/uwclrphon/CedarAI.git
cd CedarAI
```

2. **安装依赖**
```bash
# 使用requirements.txt安装所有依赖
pip install -r requirements.txt

# 或者手动安装核心依赖
pip install PySide6 openai requests
```

### 依赖说明
- **PySide6**: Qt for Python，提供GUI界面
- **openai**: OpenAI API客户端，支持多种AI模型
- **requests**: HTTP库，用于网络请求和API调用

3. **运行应用**
```bash
python -m src.main
```

### 首次运行配置
首次运行时会显示设置向导，您需要：
1. 选择AI模型提供商
2. 输入API密钥
3. 配置模型名称
4. 测试连接

## ⚙️ 配置说明

### 配置文件
- `config.json` - AI模型配置
- `modsconfig.json` - 模块配置

### config.json 示例
```json
{
  "model_url": "https://api.openai.com/v1",
  "api_key": "sk-your-api-key-here",
  "model_name": "gpt-4-turbo"
}
```

### 支持的模型URL
- OpenAI: `https://api.openai.com/v1`
- Gemini: `https://api.gemini.com/v1/`
- DeepSeek: `https://api.deepseek.com/v1/`
- Claude: `https://api.anthropic.com/v1/`
- SiliconFlow: `https://api.siliconflow.cn/v1/`
- 月之暗面: `https://api.moonshot.cn/v1/`
- Qwen: `https://dashscope.aliyuncs.com/compatible-mode/v1`

## 📦 模块系统

CedarAI 支持模块化扩展，您可以在 `mods/` 目录中添加自定义模块。

### 模块结构
```
mods/
├── FileAndRun.py    # 示例模块：文件操作和运行命令
└── YourModule.py    # 您的自定义模块
```

### 创建自定义模块
1. 在 `mods/` 目录中创建 `.py` 文件
2. 实现必要的函数
3. 通过设置界面启用模块

### 模块配置
模块状态保存在 `modsconfig.json` 中：
```json
{
  "mods": {
    "FileAndRun": {
      "enabled": true
    }
  }
}
```

## 🏗️ 项目结构

```
CedarAI/
├── src/                    # 主程序源代码
│   ├── main.py            # 程序入口
│   ├── agent.py           # ReAct代理核心
│   ├── mainui.py          # 主界面
│   ├── setup.py           # 设置界面
│   └── modcore.py         # 模块核心
├── module/                # 功能模块
│   ├── Ai_api.py          # AI API接口
│   ├── xml_commple.py     # XML处理
│   ├── system_prompt.py   # 系统提示词
│   ├── Mainui.ui          # 主界面设计文件
│   ├── setupui.ui         # 设置界面设计文件
│   └── websearch/         # 网络搜索模块
├── mods/                  # 扩展模块目录
├── res/                   # 资源文件
│   ├── image/            # 图片资源
│   ├── res_rc.py         # 资源文件
│   └── res.qrc           # Qt资源文件
├── plugins/              # 插件目录
├── config.json           # 配置文件
├── modsconfig.json       # 模块配置
└── README.md            # 本文档
```

## 🔧 开发指南

### 代码架构

#### ReAct代理 (src/agent.py)
- 实现思考-行动循环
- 工具调用系统
- 上下文管理

#### AI接口 (module/Ai_api.py)
- 统一AI模型接口
- 对话历史管理
- 错误处理

#### UI系统
- 基于PySide6的现代化界面
- 无边框窗口设计
- 响应式消息显示

### 添加新工具
1. 在 `src/agent.py` 中定义工具函数
2. 添加到工具描述列表
3. 更新系统提示词

### 添加新AI模型
1. 在 `src/setup.py` 的 `model_url_list` 中添加模型URL
2. 添加对应的设置按钮和方法

## 🌐 网络搜索功能

CedarAI 集成了强大的网络搜索功能，支持多种搜索引擎：

### 可用引擎
- **DuckDuckGo** (默认)
- **Bing**
- **Google**
- **SearXNG**

### 使用方法
```python
from module.websearch.client import WebSearch

ws = WebSearch()
results = ws.search("Python异步编程")
```

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 如何贡献
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 开发规范
- 遵循 PEP 8 代码风格
- 添加适当的注释和文档
- 确保向后兼容性
- 编写单元测试（如果适用）

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- **PySide6** - Qt for Python
- **OpenAI** - GPT API
- **所有贡献者** - 感谢你们的付出

## 📞 支持与反馈

如果您遇到问题或有建议：
1. 查看 [Issues](https://github.com/your-repo/issues) 页面
2. 提交新的 Issue
3. 或通过邮件联系我们

---

**CedarAI - 让AI助手触手可及**

*最后更新: 2024年3月*