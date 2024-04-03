import array as arr
import math as mt
import pandas as pd
# X= arr.array('d',[2.651,2.778,2.905,3.032,3.159,3.286,3.413,3.54,3.667,3.794,3.921,4.048,4.175,4.302])
# Y= arr.array('d',[2.93027,2.8834,2.64288,2.21651,1.62532,0.90269,0.09245,-0.75382,-1.5802,-2.33018,-2.95068,-3.339581,-3.63035,-3.63246])
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
X=xlsxFile['nx']
Y=xlsxFile['ny']
n=len(X)-1

def Check(X):
    X=sorted(X)
    e=0
    h=(X[1]-X[0])
    for i in range(1,n+1):
        if(h != (X[i]-X[i-1])):
            e=e+1
    if(True):
        print("Day la bai toan Noi Suy moc cach deu")
        def P(y):
            t0 = 0
            Dt = 10
            c=0
            y0=Y[0]
            Dy=0
            while(Dt>mt.pow(10,-3)):
                P=0
                for k in range(1,n+1):
                    D=1
                    L=1
                    for i in range(n-k+1):
                        Y[i]=Y[i+1]-Y[i]
                    if(k==1):
                        Dy=Y[0]
                        c=(y-y0)/Y[0]
                        t0=c
                        u=c
                        D=D*(t0-k+1)/k
                    else:
                        D=D*(t0-k+1)/k
                        L=L*Y[0]*D
                        u=u-L/Dy
                        Dt=u-t0
                        t0=u
            print("t=",t0)
            return X[0]+t0*h
            
        y=-3.15
        print("P(",y,") = ",P(y))
    else: print("Day KHONG la bai toan Noi Suy moc cach deu")
Check(X)  
    