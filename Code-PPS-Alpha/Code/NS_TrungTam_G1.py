import pandas as pd
import numpy as np
df_data = pd.read_excel('../Data/1.xlsx', index_col=None,header=None,dtype={'Name': str, 'Value': float})
print(df_data)
X=df_data[0].values.tolist()
Y=df_data[1].values.tolist()

X.pop(0)
Y.pop(0)
print(X)
print(Y)


# import array as arr
# # Input
# X = arr.array('d',[75,76,77,78,79,80,81,82,83,84])
# Y = arr.array('d',[2.7686,2.83267,2.90256,2.97857,3.06173,3.15339,3.25530,3.36987,3.50042,3.65186])
n= len(X)-1
m= len(Y)-1

q=32
print(n)
print(m)
# Y=np.array(X)
def Check(X):
    X=sorted(X)
    e=0
    h=(X[1]-X[0])
    for i in range(1,n+1):
        if(h != (X[i]-X[i-1])):
            e=e+1
    if(True):
        print("Day la bai toan Noi Suy moc cach deu")
        # Tinh f(x)
        def P(x):
        #Khoi tao
            t=(x-X[q])/h
            P=Y[0]
            D=1
            L=1
            for k in range(1,n+1,1):
                D=D*(t-k+1)/k
                for i in range(n-k+1):
                    Y[i]=[i+1]-Y[i]
                if((k % 2) == 1):
                    L=L*(Y[-k+q]-Y[-k+1+q])*D/(2*t)
                if(k%2==0):
                    L=L*Y[-k+q]*D
                P=P+L
            print("t=",t)
            return P
        #Result:
        x=78.5
        print("P(",x,") = ",P(x))   
    else: print("Day KHONG la bai toan Noi Suy moc cach deu")
        
Check(X)