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
    a6=a7=a8=a9=a10=0
    A= arr.array('d',[])

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
                        for a in range(q+1,n):
                            a6=a6+X[i]*X[j]*X[k]*X[p]*X[q]*X[a]
                            if(n==6):
                                continue
                            for b in range(a+1,n):
                                a7=a7+X[i]*X[j]*X[k]*X[p]*X[q]*X[a]*X[b]
                                if(n==7):
                                    continue
                                for c in range(b+1,n):
                                    a8=a8+X[i]*X[j]*X[k]*X[p]*X[q]*X[a]*X[b]*X[c]
                                    if(n==8):
                                        continue
                                    for d in range(c+1,n):
                                        a9=a9+X[i]*X[j]*X[k]*X[p]*X[q]*X[a]*X[b]*X[c]*X[d]
                                        if(n==9):
                                            continue
                                        for e in range(d+1,n):
                                            a10=a10+X[i]*X[j]*X[k]*X[p]*X[q]*X[a]*X[b]*X[c]*X[d]*X[e]
                                            if(n==10):
                                                continue
    if(n==1):
        A=np.array([1,-a1])
    elif(n==2):
        A=np.array([1,-a1,a2])
    elif(n==3):
        A=np.array([1,-a1,a2,-a3])
    elif(n==4):
        A=np.array([1,-a1,a2,-a3,a4])
    elif(n==5):
        A=np.array([1,-a1,a2,-a3,a4,-a5])
    elif(n==6):
        A=np.array([1,-a1,a2,-a3,a4,-a5,a6])
    elif(n==7):
        A=np.array([1,-a1,a2,-a3,a4,-a5,a6,-a7])
    elif(n==8):
        A=np.array([1,-a1,a2,-a3,a4,-a5,a6,-a7,a8])
    elif(n==9):
        A=np.array([1,-a1,a2,-a3,a4,-a5,a6,-a7,a8,-a9])
    elif(n==10):
        A=np.array([1,-a1,a2,-a3,a4,-a5,a6,-a7,a8,-a9,a10])
    # A=np.array([1,-a1,a2,-a3,a4,-a5])
    # A.extend(add)
    # A += add
    # print("A=",A)
    return A
# X=[1,2,3,4]
# X=[1,1,1,1,1,1,1,1,1,1]
# U=mP(X)
# print(U)

# x=11
# f0=(x-1)*(x-2)*(x-3)*(x-4)
# f1=mt.pow(x,4)-10*mt.pow(x,3)+35*mt.pow(x,2)-50*x+24
# print('f0=%f, f1=%f'%(f0,f1))