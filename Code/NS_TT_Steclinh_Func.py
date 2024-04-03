def xpoly(x, y):
    n = len(x)

    # Tính bảng các hiệu phân chia Newton
    Ys = [y]
    for i in range(1, n):
        Y_row = []
        for j in range(n - i):
            Y = (Ys[i - 1][j + 1] - Ys[i - 1][j]) / (x[i + j] - x[j])
            Y_row.append(Y)
        Ys.append(Y_row)
    print(Ys[1])
    # Tạo đa thức nội suy
    def interp_poly(t):
        print("t=",t)
        result = Ys[0][0]
        term = 1
        for i in range(1, n):
            term *= (t - x[i - 1])
            result += Ys[i][0] * term
        return result

    return interp_poly

# Ví dụ sử dụng
x_values = [15,20,25,30,35,40,45,50,55]
y_values = [0.2588, 0.342,0.4226, 0.5, 0.5736, 0.6428, 0.7071, 0.766, 0.8192]

# Lấy đa thức nội suy
poly = xpoly(x_values, y_values)

# In giá trị của đa thức nội suy tại một điểm cụ thể, ví dụ 2.5
result = poly(46)
print(result)
