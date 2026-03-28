from module.Mainui_ui import *
from src.agent import ReActAgent as Agent
from src.agent import init_agent
from src.setup import SetupWindow
import sys
import json
import threading
import time
import copy
from PySide6 import QtCore, QtGui, QtWidgets

def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

class MainWindow(QMainWindow):
    update_signal = QtCore.Signal(str)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.load_config_and_init_agent()
        
        self.ui.pushButton.clicked.connect(self.clear_messages)
        self.ui.pushButton_4.clicked.connect(self.onEnterPressed)
        self.ui.pushButton_5.clicked.connect(self.open_settings)
        
        self.linelist = []
        self.linecopy = copy.deepcopy(self.linelist)
        self.update_signal.connect(self.handle_update_text)
        self.t = threading.Thread(target=self.update_textBrowser)
        self.t.daemon = True
        self.t.start()
        
    def clear_messages(self):
        """清空消息列表和显示"""
        self.linelist = []
        self.linecopy = copy.deepcopy(self.linelist)
        self.ui.textBrowser.clear()
        
    def load_config_and_init_agent(self):
        """加载配置并初始化agent"""
        try:
            config = read_config()
            api_key = config['api_key']
            base_url = config['model_url']
            model = config['model_name']
            self.agent = init_agent(model, api_key, base_url)
        except Exception as e:
            print(f"加载配置失败: {e}")
            self.agent = None
            
    def open_settings(self):
        """打开设置窗口"""
        self.settings_window = SetupWindow(self)
        self.settings_window.show()
        self.settings_window.destroyed.connect(self.on_settings_closed)
        
    def on_settings_closed(self):
        """设置窗口关闭后重新加载配置"""
        self.load_config_and_init_agent()
    def onEnterPressed(self):
        t = threading.Thread(target=self.agent.run, args=(self.ui.lineEdit.text(),self.linelist))
        t.start()
        self.ui.lineEdit.clear()
    def update_textBrowser(self):
        while True:
            if self.linelist != self.linecopy:
                css_style = '''
                <style>
                body {
                    font-family: 'Microsoft YaHei UI', sans-serif;
                    font-size: 11pt;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 10px;
                }
                .message {
                    margin-bottom: 15px;
                    max-width: 85%;
                    border-radius: 12px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }
                .message-header {
                    padding: 6px 12px;
                    font-size: 10pt;
                    font-weight: bold;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .message-content {
                    padding: 10px 15px;
                    line-height: 1.5;
                }
                .user-message {
                    margin-left: auto;
                    background: linear-gradient(135deg, #4a90e2, #357ae8);
                    color: #333;
                }
                .user-message .message-header {
                    background-color: rgba(255, 255, 255, 0.2);
                    color: #333;
                }
                .ai-message {
                    margin-right: auto;
                    background: white;
                    color: #333;
                }
                .ai-message .message-header {
                    background-color: #f0f0f0;
                    color: #666;
                }
                .thought-message {
                    background: #fff8e1;
                    border-left: 4px solid #ffc107;
                }
                .thought-message .message-header {
                    background-color: #ffecb3;
                    color: #8d6e00;
                }
                .action-message {
                    background: #e8f5e9;
                    border-left: 4px solid #4caf50;
                }
                .action-message .message-header {
                    background-color: #c8e6c9;
                    color: #2e7d32;
                }
                .final-answer {
                    background: #e3f2fd;
                    border-left: 4px solid #2196f3;
                }
                .final-answer .message-header {
                    background-color: #bbdefb;
                    color: #0d47a1;
                }
                .error-message {
                    background: #ffebee;
                    border-left: 4px solid #f44336;
                }
                .error-message .message-header {
                    background-color: #ffcdd2;
                    color: #c62828;
                }
                .message-sender {
                    font-weight: bold;
                }
                .message-time {
                    font-size: 9pt;
                    opacity: 0.8;
                }
                </style>
                '''
                
                html_content = f'''
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="UTF-8">
                {css_style}
                </head>
                <body>
                {''.join(self.linelist)}
                </body>
                </html>
                '''
                self.update_signal.emit(html_content)
                self.linecopy = copy.deepcopy(self.linelist)
            time.sleep(0.1)
    
    def handle_update_text(self, text):
        self.ui.textBrowser.setHtml(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())