import array as arr
import math as mt
# Input
X = arr.array('d',[15,20,25,30,35,40,45,50,55])
Y = arr.array('d',[0.2588,0.342,0.4226,0.5,0.5736,0.6428,0.7071,0.766,0.8192])
n= len(X)-1
# kiem tra cach deu 
def Check(X):
    X=sorted(X)
    e=0
    h=(X[1]-X[0])
    for i in range(1,n+1):
        if(h != (X[i]-X[i-1])):
            e=e+1
    if(e==0):
        print("Day la bai toan Noi Suy moc cach deu")
        # Tinh f(x)
        def P(x):
        #Khoi tao
            P=Y[0]
            D=1
            t=(x-X[0])/h
            for k in range(1,n+1,1):
                for i in range(n-k+1):
                    Y[i]=Y[i+1]-Y[i]
                D=D*(t-k+1)/k
                P=P+D*Y[0]
            return P
        #Result:
        x=14
        print("P(",x,") = ",P(x))   
    else: print("Day KHONG la bai toan Noi Suy moc cach deu")
        
Check(X)