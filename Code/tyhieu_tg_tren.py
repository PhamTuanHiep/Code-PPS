import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt

# xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
# xlsxFile.rename(str.lower, axis='columns',inplace=1)

# # print(xlsxFile)
# X=xlsxFile['x']
# Y=xlsxFile['y']

def TH(X,Y):
    n=len(Y)
    F= np.zeros((n,n))
    F[:,0]=np.copy(Y)
    for j in range(1,n):
        for i in range(0,n-j):
            F[i,j]=(F[i+1,j-1]-F[i,j-1])/(X[i+j]-X[i])
    return F
# Fx=TH(X,Y)
# print(Fx)



