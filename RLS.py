import tkinter as tk
import numpy as np
import os
import pandas as pd




from ui_test import Ui_Form
from tkinter import filedialog

def RLS_main(path1,path2,na,nb):

    f1 = open(path1, 'r')
    f2 = open(path2, 'r')



    data1 = f1.readlines()
    data2 = f2.readlines()
    z =[0]*16384
    x = [0]*16384
    # z = data1[0:16384]
    # x = data2[0:16384]
    for i in range(0,16384):
        z[i] = float(data1[i].split('\t',2)[1])
        x[i] =  float(data2[i].split('\t',2)[1])

    m1 = len(data1)
    m2 = len(data2)
    m = min(m1,m2)

    L = 4000
    n=max(na,nb)

    p = np.zeros((L+n, (na+nb), (na+nb)))
    Theta = np.zeros(((na+nb),n+L))

    Theta[:,n-1] = 0.00001


    K = np.zeros(((na+nb),n+L))
    s = [0]*(n+L)
    Inn = [0]*(n+L)
    J = [0]*(n+L)

    p[n-1,:,:] = np.diag([10000] *(na+nb))
    h = np.zeros(((na+nb),n+L))

    J[n]=0.3
    m3 = np.zeros((2,na+nb))
    m4 = np.zeros((na+nb,2))

    for k in range(n,n+L):
        for i in range(0,na):
            h[i,k] = -z[k-i-1]

        for i in range(0,nb):
            h[na+i,k] = x[k-i-1]

        h_t = h[:,k].T


        s[k] =np.matmul(h_t,np.matmul( p[k-1,:,:] , h[:,k])) +1.0

        n = np.matmul(h_t, p[k-1,:,:])
        m = np.matmul( np.matmul(h_t, p[k-1,:,:]),h[:,k] ) + 1.0

        Inn[k] = z[k] - np.matmul(h[:,k].T ,Theta[:,k-1])



        K[:,k] = np.matmul(p[k-1,:,:],h[:,k])/s[k]


        for i in range(na+nb):
            m3[0] [i] = K [i][k]
            m3[1][i] = 0
            m4[i][0] =K [i][k]
            m4[i][1] = 0

        m5 = np.matmul(m4 , m3)
        p[k,:,:] = p[k-1,:,:] -m5 *s[k]
        Theta[:,k] = Theta[:,k-1] +K[:,k] *Inn[k]
        J[k] = J[k-1] + Inn[k]**2 / s[k]


    return Theta[:,k]

def data_optimize(path1,path2,na,nb,theta):


    len2 = len(theta)
    df1 = pd.read_csv(path1, sep='\t', header=None)
    df2 = pd.read_csv(path2, sep='\t', header=None)
    len1 = len(df2)
    df3 = np.zeros((len1,2))
    df3[:,1] = df2.iloc[:,1]
    df3[:, 0] = df2.iloc[:, 0] + 1.0e-06
    data2 = df2.iloc[:,1]

    for n in range(na+nb,42768):
        data_temp = 0
        if na>0:
            for j in range(0,na):
                data_temp = data_temp -theta[j]*df3[n-j-1,1]
        if nb>0:
            for j in range(0,nb):
                data_temp = data_temp +theta[j+na]*data2[n-j-1]

        df3[n,1] = data_temp
    city = pd.DataFrame(df3[0:42768,:])
    # print(xishu)
    city.to_csv('校正后通道4数据.txt',index=False,header=False,sep='\t')
    # return city
    return ('校正后通道4数据.txt')






if __name__ == "__main__":
    # root = tk.Tk()
    # root.withdraw()
    # path1 = filedialog.askopenfilename()
    # path2 = filedialog.askopenfilename()

    path1 = 'E:/pycharmworkspace/jiaochacaiyang2/通道3数据.txt'
    path2 = 'E:/pycharmworkspace/jiaochacaiyang2/通道4数据.txt'
    path3 = 'E:/pycharmworkspace/jiaochacaiyang2/通道3数据-通道异步.txt'
    path4 = 'E:/pycharmworkspace/jiaochacaiyang2/通道4数据-通道异步.txt'


    na = 3
    nb = 8
    xishu = RLS_main(path1,path2,na,nb)
    data_optimize(path3, path4, na, nb, xishu)
    print(xishu)

