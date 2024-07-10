import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
# xlsxFile = pd.read_excel('../Data/data GK 20231 PPS.xlsx',sheet_name="Sheet1", header=0)
xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
y=xlsxFile['y']
n=len(y)
Y = np.zeros((n , n))
Y[:,0]=y
print(n)
print(Y)

def SP(Y):
    for j in range(1,n): #cot
        for i in range(j,n):#hang
            Y[i,j]=Y[i,j-1]-Y[i-1,j-1]
    return Y

print(SP(Y))



def BS(y_k):
    nY=SP(Y)
    m=n+1
    #them cot 0
    nY = np.hstack([nY, np.zeros((nY.shape[0],1), dtype=nY.dtype)])
    #them hang
    nY = np.vstack([nY, np.zeros((1,nY.shape[1]), dtype=nY.dtype)])
    nY[n,0]=y_k
    print(nY)
    for j in range(1,m):#cot
        i=n
        nY[i,j]=nY[i,j-1]-nY[i-1,j-1]
    return nY
y_k=0.866
# print(BS(y_k))
    





