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

def RK4(fy,fz,X,y0,z0,h):
    n= len(X)
    print("n:",n)
    Y= np.zeros(n+1,dtype=object)
    Y[0]=y0
    Z= np.zeros(n+1,dtype=object)
    Z[0]=z0
    x, y, z = sp.symbols('x y z')

    for k in range(0,n):

        k1=h*fy.subs({x: X[k], y: Y[k], z: Z[k]})
        l1=h*fz.subs({x: X[k], y: Y[k], z: Z[k]})

        k2=h*fy.subs({x: X[k]+h/2, y: Y[k]+k1/2, z: Z[k]+ l1/2})
        l2=h*fz.subs({x: X[k]+h/2, y: Y[k]+k1/2, z: Z[k]+ l1/2})

        k3=h*fy.subs({x: X[k]+h/2, y: Y[k]+k2/2, z: Z[k]+ l2/2})
        l3=h*fz.subs({x: X[k]+h/2, y: Y[k]+k2/2, z: Z[k]+ l2/2})

        k4=h*fy.subs({x: X[k]+h, y: Y[k]+k3, z: Z[k] + l3})
        l4=h*fz.subs({x: X[k]+h, y: Y[k]+k3, z: Z[k] + l3})


        # print("k1:",k1)
        # print("k2:",k2)
        # print("k3:",k3)
        # print("k4:",k4)


        y_value=Y[k]+ (k1+2*k2+2*k3+k4)/6
        z_value=Z[k]+ (l1+2*l2+2*l3+l4)/6

        Y[k+1] = y_value
        Z[k+1] = z_value
    print("X:",X)
    print("Y:",Y)
    print("Z:",Z)
    return Y


x, y, z = sp.symbols('x y z')
fy=z
fz= -x*z-y
X=np.copy(X_test[0:5] )
y0=0
z0=1
h=0.1
YZ=RK4(fy,fz,X,y0,z0,h)
# print("YZ=",YZ)
