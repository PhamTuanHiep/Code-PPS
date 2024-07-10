import array as arr
import math as mt
import numpy as np
import pandas as pd
import tyhieu_tg_tren as TH_UP
PI=mt.pi
xlsxFile1 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X_sin=xlsxFile1['x']
Y_sin=xlsxFile1['y']

def NSNTTienValue(x,X,Y):
    N=len(X)
    vectorA= TH_UP.TH(X,Y)[0,:]
    P=vectorA[0]
    T=1
    for i in range(0,N):
        T=T*(x-X[i])
        if(i==N-1):
            break
        P=P+T*vectorA[i+1]
    return P


# X1=np.copy(X_sin[11:20] )
# Y1=np.copy(Y_sin[11:20] )
X1=[13,14,18,19,21]
Y1=[2210,2758,5850,6878,9282]

x=13.5
print(NSNTTienValue(x,X1,Y1))



