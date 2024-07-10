import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import minimize_scalar

# Hệ số da thức ----------------------------------------------------------------------------
def mP(X):
    n=len(X)
    # A = arr.array('d',[1])
    
    a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=0
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

# ham symbol ---------------------------------------------------------------
def F(X,name):
    x = sp.symbols(name)
    f=0
    A=mP(X)
    n=len(A)
    for i in range(0,n):
        f= f+A[i]*pow(x,n-1-i)
    return f

# X=[1,1,1,1,1,1,1,1,1,1]
# print(F(X,"x"))
# tq = sp.symbols('t')
# print(sp.integrate(F(X,'t'), tq))
# print(sp.diff(F(X,'t'), tq))



#Đạo hàm da rhuc f theo data bậc cập n ------------------------------------------------------------------
def DH_dt(X,n,name):
    x = sp.symbols(name)
    f=F(X,name)
    f = sp.diff(f, x,n)
    return f

# X=[1,1,1,1,1,1,1,1,1,1]
# n=1
# name="x"
# print(DH_dt(X,n,name))

#Đạo hàm hàm symbol bất kì bậc cập n ------------------------------------------------------------------
def DH_F(F,n,name):
    x = sp.symbols(name)
    f = sp.diff(F, x,n)
    return f
#Nguyên hàm bậc cập n ------------------------------------------------------------------------
def NH(X,n,name):
    x = sp.symbols(name)
    f=F(X,name)
    f = sp.integrate(f,x,n)
    return f

# X=[1,1,1,1,1,1,1,1,1,1]
# n=2
# name="x"
# f=NH(X,n,name)
# print(f)
# # tính gia trị hàm symbol
# x = sp.symbols('x')
# x_value = 0
# result = f.subs(x, x_value)
# print("Giá trị của hàm tại x =", x_value, "là:", result)

# Tìm max,min của hàm |symbol| trên 1 đoạn -----------------------------------------------------
def Max_Min_F(F,a,b,name):
    x = sp.symbols(name)
    f = sp.lambdify(x, sp.Abs(F))
    max = - minimize_scalar(lambda x: -f(x), bounds=(a, b), method='bounded').fun
    min= minimize_scalar(f, bounds=(a, b), method='bounded').fun
    V=np.array([max,min])
    return V

# a=0
# b=2
# name='x'
# x= sp.symbols(name)
# F=24/(1+pow(x,5))
# mm=Max_Min_F(F,a,b,name)
# print("Giá trị lớn nhất/nhỏ nhất của hàm trên đoạn [", a, ",", b, "] là:", mm)