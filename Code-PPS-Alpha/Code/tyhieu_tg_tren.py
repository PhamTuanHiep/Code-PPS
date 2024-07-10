import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
import array as arr

xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# # print(xlsxFile)
X=xlsxFile['x']
Y=xlsxFile['y']

#ma tran ty hieu - moi cot la mot bac ti hieu <-> cot0=f , cot1= ty hieu bac 1
def TH(X,Y):
    n=len(Y)
    F= np.zeros((n,n))
    F[:,0]=np.copy(Y)
    for j in range(1,n):
        for i in range(0,n-j):
            F[i,j]=(F[i+1,j-1]-F[i,j-1])/(X[i+j]-X[i])
    return F

A= arr.array('d',[])
#hang dau: ty hieu x0->xk
def vectorA(X,Y):
    matrixA=TH(X,Y)
    # print(matrixA[0,:])
    n=len(Y)
    for i in range(n):
        A.append(matrixA[0,i])
    return A
A=vectorA(X,Y)
# print(A)



