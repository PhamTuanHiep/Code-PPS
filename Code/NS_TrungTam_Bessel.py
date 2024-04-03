import array as arr
import math as mt
import numpy as np
import pandas as pd
PI=mt.pi
# X= arr.array('d',[5*PI/180,10*PI/180,15*PI/180,20*PI/180,25*PI/180,30*PI/180,35*PI/180,40*PI/180])
# Y= arr.array('d',[mt.sin(X[0]),mt.sin(X[1]),mt.sin(X[2]),mt.sin(X[3]),mt.sin(X[4]),mt.sin(X[5]),mt.sin(X[6]),mt.sin(X[7])])

xlsxFile = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)
X=xlsxFile['x']
Y=xlsxFile['y']
# print("X=",X)

X=X[0:6] #index = 0 --> 19
Y=Y[0:6]
# print("X=",X)
# print("Y=",Y)

N=len(X)
n= int((N-2)/2) 
# eY=np.array([[],[]])
# oY = arr.array('d',[])
# eY = np.zeros((2, N))
# oY = np.zeros(N)

print("N=",N)
print("n=",n)

def P(t):
    eY = np.zeros((2, N))
    oY = np.zeros(N)
    nY = np.copy(Y)
    eY[0,0]=Y[n]
    eY[1,0]=Y[1+n]
    P=0
    T=1
    Z=1
    for k in range(1,2*n+1):
        for i in range(0,N-k):
            nY[i]=nY[i+1]-nY[i]
            if(k%2==0):
                p=int(k/2)
                eY[0,p]=nY[-p+n]
                eY[1,p]=nY[-p+n+1]
            else:
                p=int(k/2)
                oY[p]=nY[-p+n]
    P=(eY[0,0]+eY[1,0])/2 + (t-1/2)*oY[0]
    
    for j in range(1,n+1):
        T=T*(t-(-j+1))*(t-j)/(2*j*(2*j-1))
        Z=Z*(t-(-j+1))*(t-j)/((2*j+1)*(2*j))
        P=P+T*(eY[0,j]-eY[1,j])/2 + Z*(t-1/2)*oY[j]
    return P
# x0=45
# h=5
# for l in range(1,10):
#     t=l/10
#     x=x0+t*h
#     f=mt.sin(x*PI/180)
#     p=P(t)
#     e=abs(f-p)
#     ce=e/(f)
#     print("P(t= %2.1f)= %2.6f; e= %f, e%%= %f"%(t,p,e,ce))


#f = x^4-2x^3+5x^2-x-9
x0= 0.2
h=0.1
for l in range(1,10):
    t=l/10
    x=x0+t*h
    f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
    p=P(t)
    e=abs(f-p)
    ce=100*abs(e/f)
    print("P(t= %2.1f)= %2.6f, x=%f, f=%f ; e= %f, e%%= %f"%(t,p,x,f,e,ce))