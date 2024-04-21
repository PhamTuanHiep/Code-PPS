import array as arr
import math as mt
import numpy as np
import pandas as pd
import NS_NT_Tien as NS_NTT


df1 = pd.read_csv('../Data/Mực nước biển trung bình.txt', delimiter='\t')  # Giả sử dữ liệu được phân tách bằng tab
df1.to_excel('../Data/df1.xlsx', index=False)
# df1=df1.sort_values('temp',ascending=True)

df2 = pd.read_csv('../Data/Nhiệt độ trái đất.txt', delimiter='\t')  # Giả sử dữ liệu được phân tách bằng tab
df2.to_excel('../Data/df2.xlsx', index=False)
# df2=df2.sort_values('temp',ascending=True)

n=len(df2['temp'])

# min_df1_temp=df1['temp'].describe()['min']
# max_df1_temp=df1['temp'].describe()['max']
# print('max',max_df1_temp)
# print('min',min_df1_temp)

# new_df2=df2[( df2['temp'] >= min_df1_temp) & (df1['temp']<=max_df1_temp)]

# print(new_df2)
# print(df1)

y=df1['sea_level']
x=df1['temp']
# xs=new_df2['temp']
xs=df2['temp']
ys=arr.array('d',[])
n=len(xs)
print('xs:',xs)
for i in range(0,n):
    ys.append(NS_NTT.P(xs[i],x,y))
print('ys:',ys)

# # nX=X1.values
# nT1 = arr.array('d',[])
# nT2 = arr.array('d',[])

# n=len(Y1)


# Yindex=df2[ Y2 ==-0.348 ]
# print('Yindex:',Yindex)
# print('type:',type(Yindex))
# a=Yindex['temp']
# print(a.size)
# if a.size>0:
#     print('true')
# else:
#     print('false')
# if Yindex.size>0:
#     print('Y true')
# else:
#     print('Y false')