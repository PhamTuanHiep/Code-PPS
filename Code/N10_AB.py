import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp

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

def AB4(f,X,Y,h):
    n= len(X)
    x, y = sp.symbols('x y')
    A= arr.array('d',[55/24, -59/24, 37/24, -9/24])
    y_k1=f.subs({x: X[n-1], y: Y[n-1]})
    y_k2=f.subs({x: X[n-1-1], y: Y[n-1-1]})
    y_k3=f.subs({x: X[n-1-2], y: Y[n-1-2]})
    y_k4=f.subs({x: X[n-1-3], y: Y[n-1-3]})

    y_value=Y[n-1]+ h*(A[0]*y_k1 + A[1]*y_k2 + A[2]*y_k3 + A[3]*y_k4)
    Y=np.append(Y,y_value)
    print("y_value:",y_value)
    return Y

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
x, y = sp.symbols('x y')
f=x+y
X=np.copy(X_test[1:5] )
Y=np.copy(Y_test[1:5] )

h=0.1
nY=AB4(f,X,Y,h)
print("nY=",nY)
