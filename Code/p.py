import numpy as np
import pandas as pd

def forward_newton_interpolation(x_values, y_values):
    n = len(x_values) - 1  # Bậc của đa thức nội suy
    coefficients = np.zeros(n+1)  # Khởi tạo mảng hệ số đa thức

    # Tạo bảng các hiệu phân tiến
    for i in range(n):
        y_values = [(y_values[j+1] - y_values[j]) / (x_values[j+i+1] - x_values[j]) for j in range(n-i)]

        # Cập nhật hệ số của đa thức nội suy
        coefficients[i+1] = y_values[0]

    return coefficients

# Dữ liệu ví dụ
xlsxFile = pd.read_excel('../Data/OLS_test_Gamma.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
x_values =xlsxFile['x']
y_values =xlsxFile['y']

# Tìm hệ số của đa thức nội suy Newton tiến bậc 4
coefficients = forward_newton_interpolation(x_values, y_values)

print("Hệ số của đa thức nội suy Newton tiến bậc 4:", coefficients)



