import struct

import tkinter as tk
from base64 import encode
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
f_path1 = filedialog.askopenfilename()

f1 = open(f_path1, 'r')

f_path2 = filedialog.askopenfilename()
f2 = open(f_path2, 'r')

f3 = open("合并后数据.txt",'w+')
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

print("hello word" )


