import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import GiaiThua as GT
import P_ConvertMulToPoly as Cv_M_P
import sympy as sp
import matplotlib.pyplot as plt


xlsxFile2 = pd.read_excel('../Data/Test_ViPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def RK4(fx,fy,T,x0,y0,h):
    n= len(T)
    print("n:",n)
    X = np.zeros(n+1,dtype=object)
    X[0]=x0
    Y= np.zeros(n+1,dtype=object)
    Y[0]=y0
    x, y, t = sp.symbols('x y t')

    for k in range(0,n):

        k1=h*fx.subs({t: T[k], x: X[k], y: Y[k]})
        l1=h*fy.subs({t: T[k], x: X[k], y: Y[k]})

        k2=h*fx.subs({t: T[k] +h, x: X[k]+k1, y: Y[k]+l1})
        l2=h*fy.subs({t: T[k] +h, x: X[k]+k1, y: Y[k]+l1})


        # print("k1:",k1)
        # print("k2:",k2)
        x_value=X[k]+ (k1+k2)/2
        y_value=Y[k]+ (l1+l2)/2

        X[k+1] = x_value
        Y[k+1] = y_value
    # print("X:",X)
    # print("Y:",Y)
    plt.plot(X, Y, label='Giá trị gốc')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Nội suy Bessel')
    plt.legend()  # Hiển thị chú thích
    plt.show()


    return Y


x, y = sp.symbols('x y')
fx= x*(1-x/45)- 0.5*x*y/(1+x*x)
fy= x*y +0.3*x*y/(1+x*x)
# X=np.copy(X_test[0:5] )
x0=5.2
y0=3.6
h=0.1
T = np.linspace(0, 1000,10000)

Y=RK4(fx,fy,T,x0,y0,h)
# print("Y=",Y)
