import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import matplotlib.pyplot as plt

def mP(X):
    n=len(X)
    # A = arr.array('d',[1])
    
    a1=0#b1
    a2=0#b2
    a3=0#b3
    a4=0
    a5=0#b5
    for i in range(0,n):
        a1=a1+X[i]
        if(n==1):
            continue
        for j in range(i+1,n):
            a2=a2+X[i]*X[j]
            if(n==2):
                continue
            for k in range(j+1,n):
                a3=a3+X[i]*X[j]*X[k]
                if(n==3):
                    continue
                for p in range(k+1,n):
                    a4=a4+X[i]*X[j]*X[k]*X[p]
                    if(n==4):
                        continue
                    for q in range(p+1,n):
                        a5=a5+X[i]*X[j]*X[k]*X[p]*X[q]
                        if(n==5):
                            continue
    A=np.array([1,-a1,a2,-a3,a4,-a5])
    # A.extend(add)
    # A += add
    # print("A=",A)
    return A
# X=[1,2,3,4]
# print(2*mP(X))

# x=11
# f0=(x-1)*(x-2)*(x-3)*(x-4)
# f1=mt.pow(x,4)-10*mt.pow(x,3)+35*mt.pow(x,2)-50*x+24
# print('f0=%f, f1=%f'%(f0,f1))