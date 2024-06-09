import pandas as pd
import numpy as np
import array as arr
import math as mt
import N5_BinhPhuongToiThieu_DaThuc as BPTTDT
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
# xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx', index_col=None,header=None,dtype={'Name': str, 'Value': float})
# xlsxFile = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)


def BPTT_Emu(X,Y):
    n=1 # bac da thuc
    D=0 # phan cong them
    x=2 # Neu can tim y ung voiw x thi dung
    U=BPTTDT.BPTT_DaiSo(n,X,Y)# he so bieu thuc
    a=mt.exp(U[0,0]) #tham so a
    b=U[1,0]
    y=a*mt.exp(b*x)-D
    print("U=",U)
    print("a=",a)
    print("b=",b)
    print("y=",y)


X=np.copy(xlsxFile['ex'][0:7])
Y=np.copy(xlsxFile['z'][0:7])
BPTT_Emu(X,Y)
