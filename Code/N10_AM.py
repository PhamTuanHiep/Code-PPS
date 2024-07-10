import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp
import N9_RK4 as RK
xlsxFile2 = pd.read_excel('../Data/Test_ViPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def AB4(f,X,Y,h):
    n= len(X)
    x, y = sp.symbols('x y')
    A= arr.array('d',[1901/720, -2774/720, 2616/720, -1274/720, 251/720])
    y_k1=f.subs({x: X[n-1], y: Y[n-1]})
    y_k2=f.subs({x: X[n-1-1], y: Y[n-1-1]})
    y_k3=f.subs({x: X[n-1-2], y: Y[n-1-2]})
    y_k4=f.subs({x: X[n-1-3], y: Y[n-1-3]})
    y_k5=f.subs({x: X[n-1-4], y: Y[n-1-4]})


    y_value=Y[n-1]+ h*(A[0]*y_k1 + A[1]*y_k2 + A[2]*y_k3 + A[3]*y_k4 + A[4]*y_k5)
    Y=np.append(Y,y_value)
    print("y_value:",y_value)
    return Y

def AB4(f,X,y0,h,e):
    n= len(X)
    x, y = sp.symbols('x y')
    Y= np.zeros(n+1,dtype=object)
    Y[0]=y0
    A= arr.array('d',[9/24, 19/24, -5/24, 1/24])
    Y= RK.RK4(f,X[0:4],y0,h)
    y0= f.subs({x: X[0], y: y0})
    y1=Y[1]
    y2=Y[2]
    for k in range(3,n):
        xicma = h*(A[1]*y2 + A[2]*y1 + A[2]*y0) 
        epsi = 10
        s=0
        Ys= arr.array('d',[])

        while epsi > e:
            if(s==0):
                y3 = y2+ A[0]*h*f.subs({x: X[k], y: y2}) + xicma
                Ys.append( y3)
                s=s+1
            else:
                y3 = y2+ A[0]*h*f.subs({x: X[k], y: y3}) +xicma
                Ys.append( y3)
                epsi = abs(Ys[s] - Ys[s-1])
                s=s+1
        y4= Ys[s-1]
        Y = np.append(Y,y4)
        y0=y1
        y1=y2
        y2=y3
        y3= y4
    return Y

x, y = sp.symbols('x y')
f=x+y
X=np.copy(X_test[0:11] )
y0=1
h=0.1
e= pow(10,-4)
Y=AB4(f,X,y0,h,e)
print("Y=",Y)


def AB3(f,X,Y,h):
    n= len(X)
    x, y = sp.symbols('x y')
    A= arr.array('d',[23/12, -16/12, 5/12])
    y_k1=f.subs({x: X[n-1], y: Y[n-1]})
    y_k2=f.subs({x: X[n-1-1], y: Y[n-1-1]})
    y_k3=f.subs({x: X[n-1-2], y: Y[n-1-2]})

    y_value=Y[n-1]+ h*(A[0]*y_k1 + A[1]*y_k2 + A[2]*y_k3)
    Y=np.append(Y,y_value)
    print("y_value:",y_value)
    return Y

def AB2(f,X,Y,h):
    n= len(X)
    x, y = sp.symbols('x y')
    A= arr.array('d',[3/2, -1/2])
    y_k1=f.subs({x: X[n-1], y: Y[n-1]})
    y_k2=f.subs({x: X[n-1-1], y: Y[n-1-1]})

    y_value=Y[n-1]+ h*(A[0]*y_k1 + A[1]*y_k2)
    Y=np.append(Y,y_value)
    print("y_value:",y_value)
    return Y
# x, y = sp.symbols('x y')
# f=x+y
# X=np.copy(X_test[1:5] )
# Y=np.copy(Y_test[1:5] )

# h=0.1
# nY=AB4(f,X,Y,h)
# print("nY=",nY)
