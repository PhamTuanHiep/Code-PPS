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

def Euler_normal(f,X,y0,h,e,p):
    print("f:",f)
    n =len(X)
    print("n:",n)
    Y= np.zeros(n)
    Y[0]=y0
    x, y = sp.symbols('x y')
   
    Ym= arr.array('d',[])

    for k in range(0,n-1):
        
        f0 = f.subs({x: X[k], y: Y[k]})
        if(k==0):
            equation=  Y[k] +h*f0 - y
            #rut y
            solutions = sp.solve(equation, y)
            ymk= solutions[0].subs(x,X[k+1])
            Ym.append(ymk)
        else:
            err=10
            m=0
            while err>e:
                m=m+1
                # f0 = f.subs({x: X[p-1], y: Y[p-1]})
                f1 = f.subs({x: X[k+1], y: Ym[m-1]})
                equation=  Y[k] +h/2*(f0+f1) - y
                #rut y
                solutions = sp.solve(equation, y)
                ymk=solutions[0].subs(x,X[p])
                Ym.append(ymk)
                err= abs(Ym[m]-Ym[m-1])
                # print("err:",err)
                print("m:",m)
            Y[k+1]=Ym[m]
    return Y

x, y = sp.symbols('x y')
f=x+y
X=np.copy(X_test[0:11] )
y0=1
h=0.05
e=pow(10,-4)
p=1
Y=Euler_normal(f,X,y0,h,e,p)
print("Y=",Y)


