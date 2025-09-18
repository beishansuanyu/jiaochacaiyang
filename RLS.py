import struct
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from datacombin import filecombin
from PyQt6.QtCore import pyqtSignal,QObject
import tkinter as tk
from ui_test import Ui_Form
from tkinter import filedialog
import os
from PyQt6 import QtCore, QtGui, QtWidgets

root = tk.Tk()
root.withdraw()


class MyMainForm( QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # self.textEdit.toPlainText()
        self.textEdit.setPlainText("helloworld")

    def selectfile1(self, parent=None):

        f_path1 = filedialog.askopenfilename()
        print(f_path1)
        self.textEdit.setPlainText(f_path1)

    def selectfile2(self, parent=None):

        f_path2 = filedialog.askopenfilename()
        print(f_path2)
        self.textEdit_2.setPlainText(f_path2)

    def selectfile3(self, parent=None):

        f_path3 = filedialog.askopenfilename()
        print(f_path3)
        self.textEdit_4.setPlainText(f_path3)


    def selectfile4(self, parent=None):

        f_path4 = filedialog.askopenfilename()
        print(f_path4)
        self.textEdit_3.setPlainText(f_path4)

    def dataanalyse(self, parent=None):

        print("helloworld")

    def datareform(self, parent=None):
        print("helloworld")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainForm()
    # f1 = window.file_name1
    # f2 = window.file_name2
    window.show()
    app.exec()




