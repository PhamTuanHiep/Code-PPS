import pandas as pd
import numpy as np
import array as arr
import math as mt
import N5_BinhPhuongToiThieu_DaThuc as BPTTDT
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
# xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx', index_col=None,header=None,dtype={'Name': str, 'Value': float})
# xlsxFile = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)


def BPTT_Xmu(X,Y):
    n=1 # bac da thuc
    x=5 # Neu can tim y ung voi x thi dung
    U=BPTTDT.BPTT_DaiSo(n,X,Y)# he so bieu thuc
    a=mt.exp(U[0,0]) #tham so a
    b=U[1,0]
    y=a*pow(x,b)
    print("U=",U)
    print("a=",a)
    print("b=",b)
    print("y=",y)


X=np.copy(xlsxFile['lnx'][0:5])
Y=np.copy(xlsxFile['lny'][0:5])
BPTT_Xmu(X,Y)
