import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp
PI=mt.pi

xlsxFile2 = pd.read_excel('../Data/Test_ViPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def CacMoc(a,b,n):
    X= np.zeros(n)
    for i in range(0,n):
        X[i] = 0.5*((b-a)*mt.cos((2*i+1)/(2*n+2)*PI)+(b+a))
    return X
a=-1
b=1
n=11
M = CacMoc(a,b,n)
print("M=",M)