import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
from sp_tg_tren import SP

# xlsxFile = pd.read_excel('../Data/data GK 20231 PPS.xlsx',sheet_name="Sheet1", header=0)
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
X=xlsxFile['nx']
y=xlsxFile['ny']
print('y1=',y)

# X=X[1:10]
# y=y[1:10]
n=len(y)
print('y2=',y)
print('n=',n)
Y = np.zeros((n , n))
Y[:,0]=y
print(Y)

def SP(oY):
    for j in range(1,n): #cot
        for i in range(0,n-j):#hang
            oY[i,j]=oY[i+1,j-1]-oY[i,j-1]
    return Y

def P(y):
    nY=SP(Y)
    Dt = 10
    c=0
    yn=nY[n-1,0]
    t0=(y-nY[n-1,0])/nY[n-2,1]
    h=0.05
    while(Dt>mt.pow(10,-3)):
        D=1
        for k in range(2,n):
            for i in range(0,k):
                D=D*(t0+i)/(i+1)
        u=t0-nY[n-1-k,k]/nY[n-2,1]
        Dt=u-t0
        t0=u

    return X[1]+t0*h
    
y=0.8915
# print("P(",y,") = ",P(y))

    