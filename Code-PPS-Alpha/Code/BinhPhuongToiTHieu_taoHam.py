import pandas as pd
import numpy as np
import array as arr
df_data = pd.read_excel('../Data/OLS_test_Gamma.xlsx', index_col=None,header=None,dtype={'Name': str, 'Value': float})
# print(df_data)
# Cac vecto hang y, x^4, x^3,... not handled yet
Y=df_data[1].values.tolist()
X1=df_data[0].values.tolist()
X4=df_data[2].values.tolist()
X3=df_data[3].values.tolist()
X2=df_data[4].values.tolist()
# Cac vecto hang y, x^4, x^3,... had been handled yet

Y.pop(0)
X4.pop(0)
X3.pop(0)
X2.pop(0)
X1.pop(0)
print('X2 = ',X2)

X0 = arr.array('d',[])
n= len(X1)
print('n=',n)
for i in range(0,n):
    X0.append(1)
# Y=np.array([Y])
# X4=np.array([X4])
# X3=np.array([X3])
# X2=np.array([X2])
# X1=np.array([X1])
# X0=np.array([X0])
MT = np.array([X4,X3,X2,X1,X0])
M = MT.transpose()
f=np.array([Y]).transpose()
# print('f = ',f)
M_1= np.linalg.pinv(MT@M)
print(M_1)
u = M_1@MT@f
print('u=',u[1])
t=1/2
f_x1 = u[4] + u[3]*t+u[2]*pow(t,2)+u[1]*pow(t,3)+u[0]*pow(t,4)
print('f_x1 = ',f_x1)

# print('M = ',M)
# print('MT = ',MT)

