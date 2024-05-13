import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
PI=mt.pi


xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X1=xlsxFile1['x']
Y1=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X2=xlsxFile2['x']
Y2=xlsxFile2['y']



def P_NT_Lui_CD(t,X,Y):
    N=len(X)
    n= int(N-1) 
    dY= sp_up.SP(Y)

    P=dY[n,0]
    T=1
    for k in range(1,n+1):
        T=T*(t+(k-1))/k
        P=P+T*dY[n-k,k]
    return P

# f=sin(x) /=/-----------------------------------------
x0=45
h=5
X1=X1[6:10] #index = 0 --> 19 /7->11
Y1=Y1[6:10]
for l in range(1,10):
    t=l/10
    x=x0+t*h
    f=mt.sin(x*PI/180)
    p=P_NT_Lui_CD(t,X1,Y1)
    e=abs(f-p)
    ce=100*abs(e/f)
    # print("P(t= %2.1f)= %2.8f, x=%2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(t,p,x,f,e,ce))


#f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------
x0= 1.7
h=0.1
X2=X2[14:18] #index = 0 --> 5
Y2=Y2[14:18]
for l in range(1,10):
    t=l/10
    x=x0+t*h
    f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
    p=P_NT_Lui_CD(t,X2,Y2)
    e=abs(f-p)
    ce=100*abs(e/f)
    # print("P(t= %2.1f)= %2.8f, x=%2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(t,p,x,f,e,ce))
