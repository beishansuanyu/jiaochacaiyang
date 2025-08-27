# import struct

import tkinter as tk
# from base64 import encode
from tkinter import filedialog
# import os


def filecombin(f_path1, f_path2):
    f1 = open(f_path1, 'r')

    f2 = open(f_path2, 'r')

    f3 = open("合并后数据.txt", 'w+')
    m1 = f1.readline()
    m2 = f2.readline()
    while (m1 != '' and m2 != ''):
        f3.write(m1)
        f3.write(m2)
        m1 = f1.readline()
        m2 = f2.readline()

    f1.close()
    f2.close()
    f3.close()

    print("数据合并完成")





if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    f_path1 = filedialog.askopenfilename()
    f_path2 = filedialog.askopenfilename()
    filecombin(f_path1 , f_path2)


