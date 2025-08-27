import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from datacombin import filecombin
from PyQt5.QtCore import pyqtSignal,QObject

class FileSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件选择器示例")
        self.setGeometry(200, 200, 600, 400)
        self.initUI()


    def initUI(self):
        self.btn1 = QPushButton("选择文件1", self)
        self.btn1.setGeometry(150, 100, 100, 50)
        self.btn1.clicked.connect(self.open_file1)

        self.lable1 = QLabel(self)
        self.lable1.setGeometry(0, 150, 600, 50)
        self.lable1.setText("文件1：")


        self.btn2 = QPushButton("选择文件2", self)
        self.btn2.setGeometry(150, 200, 100, 50)
        self.btn2.clicked.connect(self.open_file2)

        self.lable2 = QLabel(self)
        self.lable2.setGeometry(0, 250, 600, 50)
        self.lable2.setText("文件1")


# 创建按钮


    def open_file1(self):
        file_name1, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "所有文件 (*);;文本文件 (*.txt)"
        )
        self.file_name1 = file_name1
        if file_name1:
            print(f"选择的文件1路径：{file_name1}")
        self.lable1.setText(f"文件1：{file_name1}")

    def open_file2(self):
        file_name2, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "所有文件 (*);;文本文件 (*.txt)"
        )
        self.file_name2 = file_name2
        if file_name2:
            print(f"选择的文件1路径：{file_name2}")
        self.lable2.setText(f"文件2：{file_name2}")


# 打开文件选择对话框


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSelector()
    # f1 = window.file_name1
    # f2 = window.file_name2
    window.show()
    app.exec_()
    filecombin(window.file_name1, window.file_name2)