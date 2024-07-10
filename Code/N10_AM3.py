import numpy as np

def f(x, y):
    """ Định nghĩa phương trình vi phân y' = f(x, y) """
    return x+y  # Ví dụ hàm vi phân

def adam_bashforth_3(f, x0, y0, h, n):
    """
    Phương pháp Adams-Bashforth bậc 3 để tính giá trị ước lượng.
    """
    # Khởi tạo các giá trị
    x_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    x_values[0] = x0
    y_values[0] = y0

    # Tính các giá trị bằng phương pháp Runge-Kutta bậc 4 để có các giá trị khởi đầu
    def rk4_step(f, x, y, h):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    for i in range(2):
        y_values[i+1] = rk4_step(f, x_values[i], y_values[i], h)
        x_values[i+1] = x_values[i] + h

    # Áp dụng phương pháp Adams-Bashforth bậc 3
    for i in range(2, n):
        y_values[i+1] = (y_values[i] + h * (23*f(x_values[i], y_values[i]) -
                                             16*f(x_values[i-1], y_values[i-1]) +
                                             5*f(x_values[i-2], y_values[i-2])) / 12)
        x_values[i+1] = x_values[i] + h

    return x_values, y_values

def adam_moulton_3(f, x0, y0, h, n):
    """
    Phương pháp Adams-Moulton bậc 3 để cải thiện giá trị ước lượng.
    """
    # Khởi tạo các giá trị
    x_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    x_values[0] = x0
    y_values[0] = y0

    # Tính các giá trị bằng phương pháp Runge-Kutta bậc 4 để có các giá trị khởi đầu
    def rk4_step(f, x, y, h):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    for i in range(2):
        y_values[i+1] = rk4_step(f, x_values[i], y_values[i], h)
        x_values[i+1] = x_values[i] + h

    # Áp dụng phương pháp Adams-Bashforth bậc 3 để tính giá trị ước lượng
    y_estimated = np.zeros(n+1)
    for i in range(2, n):
        y_estimated[i+1] = (y_values[i] + h * (23*f(x_values[i], y_values[i]) -
                                                16*f(x_values[i-1], y_values[i-1]) +
                                                5*f(x_values[i-2], y_values[i-2])) / 12)
        x_values[i+1] = x_values[i] + h

    # Áp dụng phương pháp Adams-Moulton bậc 3 để cải thiện giá trị
    for i in range(2, n):
        y_values[i+1] = y_values[i] + h * (5*f(x_values[i+1], y_estimated[i+1]) +
                                            8*f(x_values[i], y_values[i]) -
                                            f(x_values[i-1], y_values[i-1])) / 12

    return x_values, y_values

# Giá trị ban đầu
x0 = 0
y0 = 1
h = 0.1
n = 10 # so doan

# Tính giá trị với phương pháp Adams-Bashforth bậc 3
x_values, y_values = adam_bashforth_3(f, x0, y0, h, n)

print("Kết quả với phương pháp Adams-Bashforth bậc 3:")
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.6f}")

# Tính giá trị với phương pháp Adams-Moulton bậc 3
x_values, y_values = adam_moulton_3(f, x0, y0, h, n)

print("\nKết quả với phương pháp Adams-Moulton bậc 3:")
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.6f}")
