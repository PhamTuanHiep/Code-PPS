import array as arr
import math as mt
import numpy as np
import pandas as pd
import sp_tg_tren as sp_up
import matplotlib.pyplot as plt
# A1= arr.array('d',[2,4])
# A2 = arr.array('d',[5, -6])
# a=np.array(A1)
# b=a.transpose()
# print(b)

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
X=[1,2,3,4]
# del X[2]
# print(X.pop(2))

# v1= np.array([1,2,3,4])
# v2=np.delete(v1,1)
# v3= np.array([3,3,2,2])
# print(v2)
# print(v1+2*v1)

# sqA=np.power(v1,v3)
# print(sqA)
# v3T=np.array([v3]).transpose()
# print('v3T = ',v3T)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Khai báo mảng cần ghép vào (phải có số phần tử bằng số hàng của ma trận)
array = np.array([7, 8])
# Chuyển đổi mảng thành dạng cột
# array = array[:, np.newaxis]
array=np.array([array]).transpose()
array = np.power(array,2)
# Ghép mảng vào ma trận theo cột
result = np.hstack((matrix, array))

print(result)

# import numpy as np

# # Khai báo mảng ban đầu
# my_array = np.array([2, 3, 4, 5])

# # Phần tử cần chèn
# element = 1

# # Chèn phần tử vào đầu mảng
# new_array = np.insert(my_array, 0, element)

# print(new_array)
