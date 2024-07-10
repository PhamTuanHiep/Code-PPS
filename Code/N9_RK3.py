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

def RK4(f,X,y0,h):
    n= len(X)
    print("n:",n)
    Y= np.zeros(n+1,dtype=object)
    Y[0]=y0
    x, y = sp.symbols('x y')

    for k in range(0,n):
        print("X[k]:",X[k])
        print("Y[k]:",Y[k])

        k1=h*f.subs({x: X[k], y: Y[k]})
        k2=h*f.subs({x: X[k]+h/2, y: Y[k]+k1/2})
        k3=h*f.subs({x: X[k]+h, y: Y[k]-k1+2*k2})

        print("k1:",k1)
        print("k2:",k2)
        print("k3:",k3)

        y_value=Y[k]+ (k1+4*k2+k3)/6
        Y[k+1] = y_value
        print("Y:",Y)

    return Y


x, y = sp.symbols('x y')
f=x+y
X=np.copy(X_test[0:5] )
y0=1
h=0.1
Y=RK4(f,X,y0,h)
print("Y=",Y)
