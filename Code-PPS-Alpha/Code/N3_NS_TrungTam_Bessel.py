import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
PI=mt.pi

xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X_sin=xlsxFile1['x']
Y_sin=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_func=xlsxFile2['x']
Y_func=xlsxFile2['y']

def BesselValue(u,X,Y):
    N=len(X)
    n= int((N-2)/2) 
    dY= sp_up.SP(Y)
    P=(dY[n,0]+dY[1+n,0])/2 +u*dY[n,1]
    T=1
    Z=u
    for i in range(1,n+1):
        T=T*(pow(u,2)-pow(i-1/2,2))/(2*i*(2*i-1))
        Z=Z*(pow(u,2)-pow(i-1/2,2))/((2*i+1*2*i))
        P=P+T*(dY[-i+n,2*i]+dY[-i+1+n,2*i])/2+ Z*dY[-i+n,2*i+1]
    return P

# f=sin(x) /=/-----------------------------------------
x0=45
h=5 
X1=np.copy(X_sin[8:12] )#index =  7->10 ,4 moc
Y1=np.copy(Y_sin[8:12] )

#f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------
# x0= 0.8
# h=0.1
# X1=np.copy(X_func[7:11] )#index =  7->10
# Y1=np.copy(Y_func[7:11] )
for l in range(1,10):
    t=l/10
    x=x0+t*h
    u=t-1/2
    f=mt.sin(x*PI/180)
    # f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
    p=BesselValue(u,X1,Y1)
    e=abs(f-p)
    ce=100*abs(e/f)
    print("P(t= %2.1f)= %2.8f, x=%2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(t,p,x,f,e,ce))
