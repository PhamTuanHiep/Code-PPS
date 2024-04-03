import array as arr
import math as mt
PI=mt.pi
arr_X= arr.array('d',[5*PI/180,7*PI/180,9*PI/180,11*PI/180])
arr_Y= arr.array('d',[mt.sin(arr_X[0]),mt.sin(arr_X[1]),mt.sin(arr_X[2]),mt.sin(arr_X[3])])
arr_L = arr.array('d',[])
# print(arr_Y)
n=len(arr_X)
def L(x):
    P=0
    for a in range(n):
        M1=1
        M2=1
        for b in range(n):
            if(a==b):
                continue
            M1=M1*(x-arr_X[b])
            M2=M2*(arr_X[a]-arr_X[b])
        # arr_L.append(M1/M2)
        P=P+(M1/M2)*arr_Y[a]
    # print(arr_L)
    return P
a=6*PI/180
print("L(",a,") = ",L(a))
