import numpy as np
import scipy.optimize as opt
import pandas as pd


xlsxFile2 = pd.read_excel('../Data/Test_ViPhan.xlsx',sheet_name="Sheet1", header=0)
xlsxFile2.rename(str.lower, axis='columns',inplace=1)
X_test=xlsxFile2['x']
Y_test=xlsxFile2['y']

def implicit_euler(f, y0, h,X):
    # Số bước thời gian
    # N = int((t_end - t0) / h)
    
    # Tạo mảng lưu nghiệm
    # t_values = np.linspace(t0, t_end, N+1)
    t_values = X
    n=len(X)
    N=n-1
    y_values = np.zeros(n)
    
    # Điều kiện ban đầu
    y_values[0] = y0
    
    # Hàm để tìm nghiệm tại bước n+1
    def func(y_next, t_next, y_current):
        return y_next - y_current - h * f(t_next, y_next)
    
    # Dùng Newton-Raphson để tìm y_{n+1} tại mỗi bước
    for n in range(N):
        t_current = t_values[n]
        t_next = t_values[n+1]
        y_current = y_values[n]
        
        # Dùng scipy.optimize.newton để tìm nghiệm
        y_next = opt.newton(func, y_current, args=(t_next, y_current))
        y_values[n+1] = y_next
    
    return t_values, y_values

# Ví dụ hàm f(t, y) = -y (giải phương trình vi phân dy/dt = -y)
def f(t, y):
    return t*y/2

# Điều kiện ban đầu
y0 = 1
h = 0.1

# Gọi hàm Euler ẩn
X=np.copy(X_test[0:11] )

t_values, y_values = implicit_euler(f, y0, h,X)

# In kết quả
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.4f}")

# Vẽ đồ thị
import matplotlib.pyplot as plt

plt.plot(t_values, y_values, label='Euler ẩn')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
