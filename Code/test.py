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

import pandas as pd

# Đọc dữ liệu từ file văn bản
data = pd.read_csv('../Data/Mực nước biển trung bình.txt', delimiter='\t')  # Giả sử dữ liệu được phân tách bằng tab

data.to_excel('data.xlsx', index=False)

print(data)
