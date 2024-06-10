import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
PI=mt.pi

xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X_sin=xlsxFile1['x']
Y_sin=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_func=xlsxFile2['x']
Y_func=xlsxFile2['y']

xlsxFile2 = pd.read_excel('../Data/Test_DaoHam.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['ny']

def DaoHamValue(t,h,X,Y):
    N=len(X)
    n=N-1
    a=1
    A= arr.array('d',[])
    B = np.zeros(N)
    C = np.zeros(N)
    P=0
    for i in range(0,N):
        J= arr.array('d',[])
        a=pow(-1,n-i)/(GT.GiaiThua(i)*GT.GiaiThua(n-i))
        # tach tich cua t thanh da thuc
        for j in range(0,N):
            if(j!=i):
                J.append(j)
        A= Cv_M_P.mP(J)
        B=B+a*Y[i]*A
    print("he so cua da thuc t truoc khi dao ham la \n",B)
    for i in range(0,N):
        k= N-1-i
        C[i]=k*B[i]
        if(i!=N-1):
            P=P+C[i]*pow(t,k-1)
    print("he so cua da thuc t sau dao ham la \n",C)
    return P/h

t=3
h=1
X=X_test[0:4]
Y=Y_test[0:4]

P= DaoHamValue(t,h,X,Y)
print(P)