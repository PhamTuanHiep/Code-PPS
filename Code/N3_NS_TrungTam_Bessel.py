import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp

xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X_sin=xlsxFile1['x']
Y_sin=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/de1CK20232PPS.xlsx',sheet_name="Sheet1", header=0)

# xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
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

def Bessel(X,Y):
    N=len(X)
    n= int((N-2)/2) 
    dY= sp_up.SP(Y)
    A_even =np.zeros(n+1)#hs chan
    A_odd =np.zeros(n+1) #hs le
    A =np.zeros(2*n+2) # hs da thuc cua tung tich
    B = np.zeros((n+1, n+1))#ma tran he so da thuc u
    I =arr.array('d',[])
    for k in range(0,n+1):
        A_even[k]= (dY[-k+n,2*k]+dY[-k+1+n,2*k])/(2*GT.GiaiThua(2*k))
        A_odd[k]= dY[-k+n,2*k+1]/GT.GiaiThua(2*k+1)
        if(k==0):
            B[0,0]=1
        else:
            I.append(k-1+1/2)
            temp = np.flip(Cv_M_P.mP(I))
            m = len(temp)
            for i in range(0,m):
                B[k,i]=temp[i]
    B_even= np.dot(A_even.transpose(),B)
    B_odd= np.dot(A_odd.transpose(),B)
    u = sp.symbols("u")
    for p in range(0,n+1):
            A[2*p]=B_even[p]
            A[2*p+1]=B_odd[p]
            F=A[2*p]*pow(u,2*p)+A[2*p+1]*pow(u,2*p+1)
    print("F=",F)
    return A



# f=sin(x) /=/-----------------------------------------
# x0=45
# h=5 
# X1=np.copy(X_sin[8:12] )#index =  7->10 ,4 moc
# Y1=np.copy(Y_sin[8:12] )

#f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------

X1=np.copy(X_func[18:25] )
Y1=np.copy(Y_func[18:25] )
# print("Y1=",Y1)
x0=0.5
x=0.6
h=0.1
u= (x-x0)/h-1/2

print("-------------------------------------------------------------------------------")
A=Bessel(X1,Y1)
print("A=",A)

# p=A[0]+A[1]*u+A[2]*pow(u,2)+A[3]*pow(u,3)+A[4]*pow(u,4)+ A[5]*pow(u,5) 
p=BesselValue(u,X1,Y1)
f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
e=abs(f-p)
ce=100*abs(e/f)
print("P(u= %2.1f)= %2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(u,p,f,e,ce))
print("-------------------------------------------------------------------------------")
