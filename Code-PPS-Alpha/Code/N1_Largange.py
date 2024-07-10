import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import matplotlib.pyplot as plt
import P_ConvertMulToPoly as Cv_M_P


xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X_sin=xlsxFile1['x']
Y_sin=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_func=xlsxFile2['lx']
Y_func=xlsxFile2['ly']


def P_Largange_Vl(x,X,Y):
    N=len(X)
    # print("N=",N)
    A = arr.array('d',[])
    P=0
    L=1
    M=1
    for j in range(0,N):
        for i in range(0,N):
            if(i != j):
                L=L*(x-X[i])/(X[j]-X[i])
                M=M*1/(X[j]-X[i])
        P=P+L*Y[j]
        L=1
        A.append(Y[j]*M)
        M=1
    # print("A=",A)
    return P


#-------------------------------------------------------------------------------------------------------------
# Chi dung de tim da thuc bac < 5
def P_Largange(X,Y):
    N=len(X)
    A = arr.array('d',[])
    P=0
    M=1
    # tim so hang
    for j in range(0,N):
        for i in range(0,N):
            if(i != j):
                M=M*1/(X[j]-X[i])
        A.append(Y[j]*M)
        M=1
    # print("A=",A)
    # tim da thuc
    Arr=0
    for j in range(0,N):
        X_cp=np.delete(X,j)
        Arr+=A[j]*Cv_M_P.mP(X_cp)
    # print("Arr",Arr)
    return Arr
X1=np.copy(X_func[0:5] )#index =  7->10->stt: 6-9
Y1=np.copy(Y_func[0:5] )
# #f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------
x=3.5
aP=P_Largange(X1,Y1)
bac=len(X1)-1
print("Cac so hang cua da thuc bac %2.0f la: "%(bac),aP)
#neu la bac 3
# f=aP[0]*pow(x,3)+aP[1]*pow(x,2)+aP[2]*pow(x,1)+aP[3]
#neu la bac 4
f=aP[0]*pow(x,4)+aP[1]*pow(x,3)+aP[2]*pow(x,2)+aP[3]*x+aP[4]
#neu la bac 5
# f=aP[0]*pow(x,5)+aP[1]*pow(x,4)+aP[2]*pow(x,3)+aP[3]*pow(x,2) +aP[4]*x + aP[5]

p=P_Largange_Vl(x,X1,Y1)
e=abs(f-p)
ce=100*abs(e/f)
print("P(x= %2.6f)= %2.8f; f=%f e= %2.8f, e%%= %2.8f"%(x,p,f,e,ce))

