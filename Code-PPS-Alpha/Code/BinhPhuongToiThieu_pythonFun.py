import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
# xlsxFile = pd.read_excel('../Data/data GK 20231 PPS.xlsx',sheet_name="Sheet1", header=0)
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
y=xlsxFile['y']
x=xlsxFile[['x','x^2','x^3','x^4']]
x=sm.add_constant(x)
reg = sm.OLS(endog=y, exog=x).fit()
print(reg.summary())

# Lấy hệ số (coefficient)
coef = reg.params
# In hệ số
print("Result da thuc:")
t=3
f_x1 = coef[0] + coef[1]*t+coef[2]*pow(t,2)+coef[3]*pow(t,3)+coef[4]*pow(t,4)
print("f1(x)=",f_x1)
print("gamma:",mt.gamma(t))
print(mt.sqrt(mt.pi))