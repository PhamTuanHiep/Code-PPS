import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
from sp_tg_tren import SP

# xlsxFile = pd.read_excel('../Data/data GK 20231 PPS.xlsx',sheet_name="Sheet1", header=0)
xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
X=xlsxFile['x']
y=xlsxFile['y']
n=len(y)
Y = np.zeros((n , n))
Y[:,0]=y
print(n)

def Gauss_II(x0):
    index=X.index[X == x0].tolist()[0]
    #defind size 2 side of new array
    d=n-1-index
    if(d > index):
        d=index
    nY=SP(Y)
    print(nY)
    P=nY[index,0]
    D1=1
    D2=1
    for k in range(1,d+1):
        D1=t+k-1
        D2=t+k
        for i in range(0,2*k-1):
            D1=D1*(D1-i)/(i+1)
        for j in range(0,2*k):
            D2=D2*(D2-i)/(i+1)
        P=P+D1*nY[-(k)+index,2*k-1] + D2*nY[-(k)+index, 2*k]
    return P
x0=30
t=4/5
print("P=",Gauss_II(x0))
