import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
PI=mt.pi
# X= arr.array('d',[5*PI/180,10*PI/180,15*PI/180,20*PI/180,25*PI/180,30*PI/180,35*PI/180,40*PI/180])
# Y= arr.array('d',[mt.sin(X[0]),mt.sin(X[1]),mt.sin(X[2]),mt.sin(X[3]),mt.sin(X[4]),mt.sin(X[5]),mt.sin(X[6]),mt.sin(X[7])])
# eY=np.array([[],[]])
# oY = arr.array('d',[])
# eY = np.zeros((2, N))
# oY = np.zeros(N)

xlsxFile1 = pd.read_excel('../Data/ham_luong_giac.xlsx',sheet_name="Sheet1", header=0)
xlsxFile1.rename(str.lower, axis='columns',inplace=1)
X1=xlsxFile1['x']
Y1=xlsxFile1['y']

xlsxFile2 = pd.read_excel('../Data/ham_da_thuc.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X2=xlsxFile2['x']
Y2=xlsxFile2['y']



def P(t,X,Y):
    N=len(X)
    n= int((N-2)/2) 
    dY= sp_up.SP(Y)

    with open("file.txt", "w") as file:
        # Ghi dữ liệu vào file
        for i in range(0,N):
            for j in range(0,N):
                file.write(str(dY[i,j])+"\t")
            file.write("\n")

    P=(dY[n,0]+dY[1+n,0])/2 +(t-1/2)*dY[n,1]
    T=1
    Z=1
    for k in range(1,n+1):
        T=T*(t+k-1)*(t-k)/(2*k*(2*k-1))
        Z=Z*(t+k-1)*(t-k)/((2*k+1)*2*k)
        P=P+T*(dY[-k+n,2*k]+dY[-k+1+n,2*k])/2+ Z*(t-1/2)*dY[-k+n,2*k+1]
    return P

# f=sin(x) /=/-----------------------------------------
x0=40
h=5
X1=X1[7:11] #index = 0 --> 19 /7->11
Y1=Y1[7:11]
for l in range(1,10):
    t=l/10
    x=x0+t*h
    f=mt.sin(x*PI/180)
    # f=1
    p=P(t,X1,Y1)
    e=abs(f-p)
    ce=100*abs(e/f)
    print("P(t= %2.1f)= %2.8f, x=%2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(t,p,x,f,e,ce))


#f = x^4-2x^3+5x^2-x-9 /=/-------------------------------------------
# x0= 0.2
# h=0.1
# X2=X2[0:6] #index = 0 --> 5
# Y2=Y2[0:6]
# for l in range(1,10):
#     t=l/10
#     x=x0+t*h
#     f=pow(x,4)-2*pow(x,3)+5*pow(x,2)-x-9
#     p=P(t,X2,Y2)
#     e=abs(f-p)
#     ce=100*abs(e/f)
#     print("P(t= %2.1f)= %2.8f, x=%2.8f, f=%2.8f ; e= %2.8f, e%%= %2.8f"%(t,p,x,f,e,ce))

    # def P(t):
#     eY = np.zeros((2, N))
#     oY = np.zeros(N)
#     nY = np.copy(Y)
#     eY[0,0]=Y[n]
#     eY[1,0]=Y[1+n]
#     P=0
#     T=1
#     Z=1
#     for k in range(1,2*n+1):
#         for i in range(0,N-k):
#             nY[i]=nY[i+1]-nY[i]
#             if(k%2==0):
#                 p=int(k/2)
#                 eY[0,p]=nY[-p+n]
#                 eY[1,p]=nY[-p+n+1]
#             else:
#                 p=int(k/2)
#                 oY[p]=nY[-p+n]
#     P=(eY[0,0]+eY[1,0])/2 + (t-1/2)*oY[0]
    
#     for j in range(1,n+1):
#         T=T*(t-(-j+1))*(t-j)/(2*j*(2*j-1))
#         Z=Z*(t-(-j+1))*(t-j)/((2*j+1)*(2*j))
#         P=P+T*(eY[0,j]-eY[1,j])/2 + Z*(t-1/2)*oY[j]
#     return P