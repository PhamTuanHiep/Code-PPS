import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
from sympy import *

xlsxFile2 = pd.read_excel('../Data/Test_TichPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def H(n):
    M=arr.array('d',[])
    
    H=0
    for i in range(0,n+1):
        J=arr.array('d',[])
        for j in range(0,n+1):
            if(j!=i):
                J.append(j)
        t = Symbol('t')
        F=Cv_M_P.F(J,'t')
        # print("F=",F)
        a=0
        b=n
        T=integrate(F, (t, a, b))
        H=pow(-1,n-i)/(n*GT.GiaiThua(i)*GT.GiaiThua(n-i))*T
        M.append(H)
    return M
# n=4
# H=H(n)
# print(H)
# print(H[0])


def I(Y,a,b):
    N=len(Y)
    n=N-1
    print("n=",n)
    h=H(n)
    I=0
    print("H=",h)
    print("H mũ", sum(h))
    for i in range(0,N):
        I=I+h[i]*Y[i]
    return (b-a)*I

Y=np.copy(Y_test[0:7])
a=0
b=1
print("I=",I(Y,a,b))