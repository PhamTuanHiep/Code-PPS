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

def XimSon2Lop(F,X,Y,a,b,d,c,n,m):
    h=(b-a)/(2*n)
    k=(d-c)/(2*m)
    Z=Z_value_table(F,X,Y,n,m)
    I=h*k*(Z[0,0]+Z[0,2]+Z[2,0]+Z[2,2] +4*(Z[0,1]+Z[1,0]+Z[2,1]+Z[1,2])+16*Z[1,1])/9
    print("n=%f, m =%f \nh=%f, k=%f"%(n,m,h,k))
    print("Z table =\n",Z)
    return I
def Z_value_table(F,X,Y,n,m):
    x,y =sp.symbols("x y")
    # tính gia trị hàm symbol
    N=2*n+1
    M=2*m+1
    Z= np.zeros((M,N))
    for i in range(0,N): #x
        for j in range(0,M):#y
            Z[i,j]=  F.subs({x: X[i], y: Y[j]})
    return Z

x,y =sp.symbols("x y")
F=1/(x*(1+y*y))
a=1 ; b=4
c=0 ; d=1
n=1 ; m=1
X=np.copy(X_test[0:3])
Y=np.copy(Y_test[0:3])
S= XimSon2Lop(F,X,Y,a,b,d,c,n,m)
print("Giá trị tích phân 2 lớp thu được:",S)