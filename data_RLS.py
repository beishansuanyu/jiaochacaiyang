import struct
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from datacombin import filecombin
from PyQt6.QtCore import pyqtSignal,QObject
import tkinter as tk
from ui_test import Ui_Form
from tkinter import filedialog
from RLS import *
from datacombin import *
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
        na = 0
        nb = 10

    def selectfile1(self, parent=None):

        self.f_path1 = filedialog.askopenfilename()
        print(self.f_path1)
        self.textEdit.setPlainText(self.f_path1)

    def selectfile2(self, parent=None):

        self.f_path2 = filedialog.askopenfilename()
        print(self.f_path2)
        self.textEdit_2.setPlainText(self.f_path2)

    def selectfile3(self, parent=None):

        self.f_path3 = filedialog.askopenfilename()
        print(self.f_path3)
        self.textEdit_4.setPlainText(self.f_path3)


    def selectfile4(self, parent=None):

        self.f_path4 = filedialog.askopenfilename()
        print(self.f_path4)
        self.textEdit_3.setPlainText(self.f_path4)

    def dataanalyse(self, parent=None):
        self.xishu = RLS_main(self.f_path1,self.f_path2,0,10)
        print("helloworld")
        self.textEdit_5.setPlainText("分析完成")

    def datareform(self, parent=None):
        f_path5 = data_optimize(self.f_path3, self.f_path4, 0, 10, self.xishu)
        filecombin (self.f_path3,f_path5)
        self.textEdit_6.setPlainText("处理完成")


        print("helloworld")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainForm()
    # f1 = window.file_name1
    # f2 = window.file_name2
    window.show()
    app.exec()




