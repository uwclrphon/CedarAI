from module.setupui_ui import *
from PySide6 import QtCore, QtGui, QtWidgets
import sys
from module import Ai_api
import json
import os

model_url_list = {
    "openai": "https://api.openai.com/v1/",
    "gemini": "https://api.gemini.com/v1/",
    "deepseek": "https://api.deepseek.com/v1/",
    "claude": "https://api.anthropic.com/v1/",
    "siliconflow": "https://api.siliconflow.cn/v1/",
    "yuezhianmian": "https://api.moonshot.cn/v1/",
    "qwen": "https://dashscope.aliyuncs.com/compatible-mode/v1",
}

class SetupWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SetupWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5,5)
        self.shadow.setBlurRadius(10)
        self.ui.frame.setGraphicsEffect(self.shadow)
        
        self.load_config()
        
        self.ui.pushButton_2.clicked.connect(self.setopenai)
        self.ui.pushButton_3.clicked.connect(self.setgemini)
        self.ui.pushButton_4.clicked.connect(self.setdeepseek)
        self.ui.pushButton_5.clicked.connect(self.setclaude)
        self.ui.pushButton_6.clicked.connect(self.setsiliconflow)
        self.ui.pushButton_7.clicked.connect(self.setyuezhianmian)
        self.ui.pushButton_8.clicked.connect(self.setqwen)
        self.ui.pushButton_9.clicked.connect(self.setother)
        self.ui.pushButton_10.clicked.connect(self.set_model_url)
        self.ui.pushButton_11.clicked.connect(self.setmodelother)
        self.ui.pushButton_12.clicked.connect(self.setmod)
        self.ui.pushButton_13.clicked.connect(self.save_mod_config)
        
    def load_config(self):
        """加载现有配置到UI"""
        if os.path.exists("config.json"):
            try:
                with open("config.json", "r") as f:
                    config = json.load(f)
                url = config.get("model_url", "")
                api_key = config.get("api_key", "")
                model = config.get("model_name", "")
                
                self.model_select = "other"
                for key, value in model_url_list.items():
                    if value == url:
                        self.model_select = key
                        break
                
                if self.model_select == "other":
                    self.ui.stackedWidget_2.setCurrentIndex(1)
                    self.ui.lineEdit_5.setText(url)
                    self.ui.lineEdit_4.setText(api_key)
                    self.ui.lineEdit_3.setText(model)
                    self.ui.label_2.setText("当前选择模型提供商：自定义")
                else:
                    self.ui.stackedWidget_2.setCurrentIndex(0)
                    self.ui.lineEdit.setText(api_key)
                    self.ui.lineEdit_2.setText(model)
                    # 根据model_select设置按钮状态
                    self.update_model_label()
            except Exception as e:
                print(f"加载配置失败: {e}")
                self.model_select = "openai"
        else:
            self.model_select = "openai"
            
    def update_model_label(self):
        """更新模型标签显示"""
        if self.model_select == "openai":
            self.ui.label_2.setText("当前选择模型提供商：openai")
        elif self.model_select == "gemini":
            self.ui.label_2.setText("当前选择模型提供商：gemini")
        elif self.model_select == "deepseek":
            self.ui.label_2.setText("当前选择模型提供商：deepseek")
        elif self.model_select == "claude":
            self.ui.label_2.setText("当前选择模型提供商：claude")
        elif self.model_select == "siliconflow":
            self.ui.label_2.setText("当前选择模型提供商：硅基流动")
        elif self.model_select == "yuezhianmian":
            self.ui.label_2.setText("当前选择模型提供商：月之暗面")
        elif self.model_select == "qwen":
            self.ui.label_2.setText("当前选择模型提供商：通义千问")
        else:
            self.ui.label_2.setText("当前选择模型提供商：自定义")
    def set_model_url(self):
        url = model_url_list[self.model_select]
        api_key = self.ui.lineEdit.text()
        model = self.ui.lineEdit_2.text()
        try:
            print(url, api_key, model)
            aiapi = Ai_api.AiModel(url, api_key, model, "")
            test = aiapi.get_response("你好，欢迎使用AI助手")
            print(test)
            #test包含Error,和错误信息
            if ("Error" in test) or ("error" in test) or ("错误" in test):
                print("api不可用")
                return
        except Exception as e:
            print("api不可用")
            return
        with open("config.json", "w") as f:
            json.dump({"model_url": url, "api_key": api_key, "model_name": model}, f)
        self.close()
        
    def setmodelother(self):
        url = self.ui.lineEdit_5.text()
        api_key = self.ui.lineEdit_4.text()
        model = self.ui.lineEdit_3.text()
        try:
            print(url, api_key, model)
            aiapi = Ai_api.AiModel(url, api_key, model, "")
            test = aiapi.get_response("你好，欢迎使用AI助手")
            print(test)
            if ("Error" in test) or ("error" in test) or ("错误" in test):
                print("api不可用")
                return
        except Exception as e:
            print("api不可用")
            return
        with open("config.json", "w") as f:
            json.dump({"model_url": url, "api_key": api_key, "model_name": model}, f)
        self.close()
    def setopenai(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "openai"
        self.update_model_label()
        
    def setgemini(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "gemini"
        self.update_model_label()
        
    def setdeepseek(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "deepseek"
        self.update_model_label()
        
    def setclaude(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "claude"
        self.update_model_label()
        
    def setsiliconflow(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "siliconflow"
        self.update_model_label()
        
    def setyuezhianmian(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "yuezhianmian"
        self.update_model_label()
        
    def setqwen(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.model_select = "qwen"
        self.update_model_label()
        
    def setother(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.model_select = "other"
        self.update_model_label()
        
    def setmod(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
        self.load_mods_config()
        
    def load_mods_config(self):
        """加载mod配置到listWidget"""
        # 设置listWidget属性以确保复选框可交互
        self.ui.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # ... (保留你原有的其他样式设置) ...
        self.ui.listWidget.setStyleSheet("""
            QListWidget::item {
                padding: 5px;
                border: 1px solid transparent;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357ae8);;
            }
            QListWidget::item:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4acfe2, stop:1 #35cae8);;
            }
        """)
        self.ui.listWidget.setSpacing(5)
        self.ui.listWidget.setGridSize(QtCore.QSize(100, 35))
        
        self.ui.listWidget.itemChanged.connect(self.on_item_changed)
        
        self.ui.listWidget.blockSignals(True)
        
        try:
            if os.path.exists("modsconfig.json"):
                try:
                    with open("modsconfig.json", "r") as f:
                        mods_config = json.load(f)
                    mods = mods_config.get("mods", {})
                    self.ui.listWidget.clear()
                    for mod_name, mod_info in mods.items():
                        item = QtWidgets.QListWidgetItem(mod_name)
                        item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                        
                        enabled = mod_info.get("enabled", False)
                        item.setCheckState(QtCore.Qt.CheckState.Checked if enabled else QtCore.Qt.CheckState.Unchecked)
                        
                        item.setSizeHint(QtCore.QSize(100, 30))
                        self.ui.listWidget.addItem(item)
                except Exception as e:
                    print(f"加载mod配置失败: {e}")
            else:
                self.ui.listWidget.clear()
                mods_dir = "mods"
                if os.path.exists(mods_dir):
                    for filename in os.listdir(mods_dir):
                        if filename.endswith(".py") and filename != "__init__.py":
                            mod_name = filename[:-3]
                            item = QtWidgets.QListWidgetItem(mod_name)
                            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                            item.setCheckState(QtCore.Qt.CheckState.Checked)
                            item.setSizeHint(QtCore.QSize(100, 30))
                            self.ui.listWidget.addItem(item)
                self.save_mod_config()
        finally:
            self.ui.listWidget.blockSignals(False)

            
    def on_item_changed(self, item):
        """当listWidget项目状态改变时调用"""
        print(f"项目 {item.text()} 状态改变: {item.checkState()}")
            
    def save_mod_config(self):
        """保存mod配置到modsconfig.json"""
        mods = {}
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            mod_name = item.text()
            enabled = item.checkState() == QtCore.Qt.CheckState.Checked
            mods[mod_name] = {"enabled": enabled}
        mods_config = {"mods": mods}
        try:
            with open("modsconfig.json", "w") as f:
                json.dump(mods_config, f, indent=4)
            print("mod配置已保存")
        except Exception as e:
            print(f"保存mod配置失败: {e}")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SetupWindow()
    sys.exit(app.exec())