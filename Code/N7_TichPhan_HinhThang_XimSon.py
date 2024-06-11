import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp

xlsxFile2 = pd.read_excel('../Data/Test_TichPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

# pp Hình Thang ----------------------------------------------------------------------
def HT(Y,h):
    n=len(Y)-1
    P=Y[0]+Y[n]
    for i in range(1,n):
        P=P+2*Y[i]
    return P*h/2
def Er_HT(F,a,b,name,h):
    n=2
    f= Cv_M_P.DH_F(F,n,name)
    print("Đạo hàm cấp %2.0f của f là"%(n),f)
    max = Cv_M_P.Max_Min_F(f,a,b,name)[0]
    E= max*(b-a)*pow(h,2)/12
    return E

# a=4.2
# b=5.4
# n=3
# h=(b-a)/n
# Y=np.copy(Y_test[0:4])
# XS = HT(Y,h)
# print("Tích phân tính theo Hình Thang = ",XS)

# name='x'
# x= sp.symbols(name)
# F= (3.5*pow(x,2)+5.1*x-4.8)/(x-0.4)
# print("Hàm gốc f:",F)
# e=Er_HT(F,a,b,name,h)
# print("Sai số tích phân tính theo Hình Thang = ",e)

# pp XimSon ----------------------------------------------------------------
def XimSon(Y,h):
    m=(len(Y)-1)/2
    N=int(2*m)
    print("2m=",N)
    P=Y[0]+Y[N]
    for i in range(1,N):
        if(i % 2 ==0):
            P=P+2*Y[i]
        else:
            P=P+4*Y[i]
    return P*h/3
def Er_XS(F,a,b,name,h):
    n=4
    f= Cv_M_P.DH_F(F,n,name)
    print("Đạo hàm cấp %2.0f của f là"%(n),f)
    max = Cv_M_P.Max_Min_F(f,a,b,name)[0]
    E= max*(b-a)*pow(h,4)/180
    return E

a=4.2
b=5.4
m=3
h=(b-a)/(2*m)
Y=np.copy(Y_test[0:7])
XS = XimSon(Y,h)
print("Tích phân tính theo XimSon = ",XS)

name='x'
x= sp.symbols(name)
F= (3.5*pow(x,2)+5.1*x-4.8)/(x-0.4)
print("Hàm gốc f:",F)
e=Er_XS(F,a,b,name,h)
print("Sai số tích phân tính theo XimSon = ",e)