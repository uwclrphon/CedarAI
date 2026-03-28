from . import setup
from . import mainui

from PySide6 import QtCore, QtGui, QtWidgets
import os
import sys

if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.getcwd(), 'config.json')):
        app = QtWidgets.QApplication(sys.argv)
        setup_window = setup.SetupWindow()
        setup_window.show()
        app.exec()
    else:
        app = QtWidgets.QApplication(sys.argv)
        main_window = mainui.MainWindow()
        main_window.show()
        app.exec()