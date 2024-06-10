import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
from sympy import *

xlsxFile2 = pd.read_excel('../Data/Test_TichPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def HT(Y,h):
    n=len(Y)-1
    P=Y[0]+Y[n]
    for i in range(1,n):
        P=P+2*Y[i]
    return P*h/2
def XimSon(Y,h):
    m=(len(Y)-1)/2
    P=Y[0]+Y[n]
    for i in range(1,2*m):
        if(i % 2 ==0):
            P=P+2*Y[i]
        else:
            P=P+4*Y[i]
    return P*h/3