
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from datacombin import filecombin
from PyQt6 import uic
from PyQt5.QtCore import pyqtSignal,QObject


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("E:/pycharmworkspace/jiaochacaiyang2/data_rls.ui")
    ui.show()

    sys.exit(app.exec_())
