import array as arr
import math as mt
import pandas as pd
import warnings 
warnings.filterwarnings("ignore")

# Input
xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)
X=xlsxFile['x']
Y=xlsxFile['y']
n= len(X) #stt

# kiem tra cach deu 
def Check(X):
    e=0
    h=(X[1]-X[0])
    for i in range(1,n): #i=1->n
        if(h - (X[i]-X[i-1]) >mt.pow(1,-3)):
            e=e+1
    if(e==0):
        print("Day la bai toan Noi Suy moc cach deu")
        # Tinh f(x)
        def P(x):
            # find index of X0
            p = X.index[X == x].tolist()[0]
            #defind size 2 side of new array
            d=n-1-p
            if(d > p):
                d=p
            
            print("index of x0:",p," & r=:",d)
            start_index = p-d
            end_index = p+d

            nX = xlsxFile['x'][start_index:end_index + 1].values
            nY = xlsxFile['y'][start_index:end_index + 1].values
            m=len(nX)
            print(nX)
            print(nY)
        #Khoi tao
            P=nY[0]
            D1=1
            D2=1
            s=1
            for k in range(0,2*d):
                for i in range(0,m-1-k):
                    nY[i]=nY[i+1]-nY[i]
                if(k%2==0):
                    index1=int(d-k/2)
                    index2= int(d-k/2-1)
                    A=(nY[index1]+nY[index2])/2
                    if(i==0):
                        D1=D1*t
                    else:
                        D1=D1*(t*t-i*i)
                    P=P+A*D1/s
                else:
                    index3=int(d-(k+1)/2)
                    B=nY[index3]
                    D2=D2*(t*t-i*i)
                    P=P+B*D2/s
                s=(s+1) 
            return P 
        #Result:
        x_0=45 #x_0 is x_0_0
        t=1/5
        h=5
        print("P(",x_0+t*h,") = ",P(x_0))  
        print("sin(",x_0+t*h,") = ",mt.sin((x_0+t*h)*mt.pi/180))  
    else: print("Day KHONG la bai toan Noi Suy moc cach deu")
        
Check(X)
print(Y)
