import array as arr
import math as mt
import numpy as np
import pandas as pd
import tyhieu_tg_tren as TH_UP

xlsxFile1 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X1=xlsxFile1['x']
Y1=xlsxFile1['y']
# X1=[13,14,18,19,21]
# Y1=[2210,2758,5850,6878,9282]


def P(x,X,Y):
    TH_Y=TH_UP.TH(X,Y)
    print(TH_Y)
    p=TH_Y[0,0]
    G=1
    n=len(Y)
    for k in range(0,n-1):
        G=G*(x-X[k])
        p=p+G*TH_Y[0,k+1]
    return p
#f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------
# x= 0.29
# f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
# p=P(x,X1,Y1)
# e=abs(f-p)
# ce=100*abs(e/f)
# print("P(x= %2.1f)= %2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(x,p,f,e,ce))
# print(P(13.5,X1,Y1))


