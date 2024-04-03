import array as arr
import math as mt
import pandas as pd
import warnings 
warnings.filterwarnings("ignore")
print(pd.__version__)

# Input
xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)
X=xlsxFile['x']
Y=xlsxFile['y']
n= len(X) #stt
m=n-1 #index
print(Y)
print(n)

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
        #Khoi tao
            P=Y[m]
            D=1
            t=(x-X[m])/h
            for k in range(1,n): #k la step = n_y
                for i in range(n-k): # i =index <n-1
                    Y[i]=Y[i+1]-Y[i]
                D=D*(t+k-1)/k
                P=P+D*Y[m-k]
            return P
        #Result:
        x=50
        print("P(",x,") = ",P(x))  
        print("sin(",x,") = ",mt.sin(x*mt.pi/180))  
    else: print("Day KHONG la bai toan Noi Suy moc cach deu")
        
Check(X)
print(Y)