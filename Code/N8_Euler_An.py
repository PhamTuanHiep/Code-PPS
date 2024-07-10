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

def Euler_normal(f,X,y0,h):
    print("f:",f)
    n =len(X)
    print("n:",n)
    Y= np.zeros(n)
    Y[0]=y0
    x, y = sp.symbols('x y')
    for k in range(0,n-1):
        equation= -y + Y[k] +h*f
        solutions = sp.solve(equation, y)
        Y[k+1]=solutions[0].subs(x,X[k+1])
    return Y

x, y = sp.symbols('x y')
f=x+y
X=np.copy(X_test[0:11] )
y0=1
h=0.05
Y=Euler_normal(f,X,y0,h)
print("Y=",Y)


