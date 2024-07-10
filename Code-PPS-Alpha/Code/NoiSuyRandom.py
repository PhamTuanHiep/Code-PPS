import array as arr
import math as mt
# Input
X = arr.array('d',[11,13,14,18,19,21])
Y = arr.array('d',[1342,2210,2758,5850,6878,9282])
F = arr.array('d',[])
n= len(X)-1 #n is index max
def P(x):
#Khoi tao
    P=Y[0]
    D=1
    for k in range(1,n+1,1):
        D=D*(x-X[k-1])
        for i in range(n-k+1):
            Y[i]=(Y[i+1]-Y[i])/(X[i+k]-X[i])
        P=P+D*Y[0]
    
    return P
x=13.5
print("P(",x,") = ",P(x))