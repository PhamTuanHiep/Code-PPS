import pandas as pd
import numpy as np
import array as arr
import math as mt
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
# xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx', index_col=None,header=None,dtype={'Name': str, 'Value': float})
# xlsxFile = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)


def BPTT_DaiSo(n,X,Y):
    # tao vecto muy size = 1xm
    mu=np.array([X]).transpose()
    # Khoi tao M la vecto cot mx1 , gia tri =1
    M = np.copy(np.power(mu,0))
    for i in range(1,n+1):
        mu_i = np.power(mu,i)
        M = np.hstack((M, mu_i))
    MT=M.transpose()
    MT_M = np.linalg.pinv(MT@M)
    Y=np.array([Y]).transpose()
    U=MT_M@MT@Y
    return U

# n=1 # bac da thuc
# U=BPTT_DaiSo(n,X,Y)
# print("U=",U)
# print(U[0,0])
# print(mt.exp(U[0,0]))


