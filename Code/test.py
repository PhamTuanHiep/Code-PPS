import numpy as np
import array as arr
# A1= arr.array('d',[2,4])
# A2 = arr.array('d',[5, -6])
# a=np.array(A1)
# b=a.transpose()
# # print(b)

# A = np.array([[1,2,3],[-1,0,4],[2,5,-1]])
# B = np.array([A1, A2])
# BT= B.transpose()
# print(B)
# print(BT)

# Q = np.linalg.pinv(B) 
# M =B@Q
# print(Q)
# print("M=",M)
# # print(A.transpose())
# ''' Output:[[11 1] [ 8 0]] '''


# # Tạo ma trận 2x3
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6]])

# print("Ma trận gốc:")
# print(matrix)
# print(matrix[1,2])


# # Mở rộng kích thước ma trận thành 3x4 bằng cách thêm hàng và cột mới
# new_rows = 3
# new_columns = 4

# # Thêm cột mới
# matrix = np.hstack([matrix, np.zeros((matrix.shape[0], new_columns), dtype=matrix.dtype)])
# # Thêm hàng mới
# matrix = np.vstack([matrix, np.zeros((new_rows,matrix.shape[1]), dtype=matrix.dtype)])


# print("\nMa trận sau khi mở rộng kích thước:")
# print(matrix)

import array as arr
import pandas as pd

# Input
xlsxFile = pd.read_excel('../Data/OLS_test.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)
X=xlsxFile['x']
Y=xlsxFile['y']
n= len(X) #stt
# print("X=",type(X))
# print("Y=",Y)
# Y= np.transpose(Y)
# print("Y=",Y)

print("Y[2]=",Y[2:5])#2->4
x0=5
# index=X.index[X == x0].tolist()[0]
# print(index)



