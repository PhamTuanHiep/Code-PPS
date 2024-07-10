import numpy as np

# Hàm để tính bảng sai phân hữu hạn
def newton_forward_diff_table(x, y):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]
    return diff_table

# Hàm để tính giá trị của x khi biết y bằng nội suy Newton ngược
def inverse_interpolation(x, y, target_y, h):
    n = len(x)
    diff_table = newton_forward_diff_table(x, y)
    
    # Tìm y gần nhất với target_y
    nearest_index = np.argmin(np.abs(y - target_y))
    
    # Bắt đầu từ chỉ số gần nhất
    p = (target_y - y[nearest_index]) / diff_table[nearest_index, 1]
    xi = x[nearest_index]
    
    for i in range(2, n):
        p_term = 1
        for j in range(1, i):
            p_term *= (p + j - 1)
        p_term /= np.math.factorial(i - 1)
        xi += p_term * diff_table[nearest_index, i]
    
    return xi

# Ví dụ dữ liệu x và y
x = np.array([20, 25, 30])
y = np.array([1.310, 1.3979, 1.4771])

# Giá trị của y mà ta muốn tìm giá trị tương ứng của x
target_y = 1.35

# Bước h (khoảng cách giữa các mốc x)
h = x[1] - x[0]

# Tính giá trị x tương ứng với target_y
inverse_x = inverse_interpolation(x, y, target_y, h)
print(f"Giá trị của x tương ứng với y = {target_y} là x ≈ {inverse_x:.6f}")
