import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa phương trình vi phân y' = f(x, y)
def f(x, y):
    return x+y # Ví dụ hàm vi phân

# Phương pháp Runge-Kutta bậc 4 để tính giá trị tiếp theo
def rk4_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h*k1/2)
    k3 = f(x + h/2, y + h*k2/2)
    k4 = f(x + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

# Phương pháp Runge-Kutta bậc 4 để tính nghiệm
def rk4(f, x0, y0, h, n):
    x_values = np.linspace(x0, x0 + n*h, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        y_values[i+1] = rk4_step(f, x_values[i], y_values[i], h)

    return x_values, y_values

# Phương pháp Adams-Bashforth bậc 3
def adams_bashforth_3(f, x0, y0, h, n):
    x_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    x_values[0] = x0
    y_values[0] = y0

    # Tính các giá trị khởi đầu bằng phương pháp Runge-Kutta bậc 4
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

# Phương pháp Adams-Moulton bậc 3
def adams_moulton_3(f, x0, y0, h, n):
    x_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    x_values[0] = x0
    y_values[0] = y0

    # Tính các giá trị khởi đầu bằng phương pháp Runge-Kutta bậc 4
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

# Tham số
x0 = 0
y0 = 1
h = 0.1
n = 10

# Tính giá trị với phương pháp Runge-Kutta bậc 4
x_values_rk4, y_values_rk4 = rk4(f, x0, y0, h, n)
print("Kết quả với phương pháp Runge-Kutta bậc 4:")
for x, y in zip(x_values_rk4, y_values_rk4):
    print(f"x = {x:.2f}, y = {y:.6f}")

# Tính giá trị với phương pháp Adams-Bashforth bậc 3
x_values_ab3, y_values_ab3 = adams_bashforth_3(f, x0, y0, h, n)
print("Kết quả với phương pháp Runge-Kutta bậc 4:")
for x, y in zip(x_values_ab3, y_values_ab3):
    print(f"x = {x:.2f}, y = {y:.6f}")

# Tính giá trị với phương pháp Adams-Moulton bậc 3
x_values_am3, y_values_am3 = adams_moulton_3(f, x0, y0, h, n)
print("Kết quả với phương pháp Runge-Kutta bậc 4:")
for x, y in zip(x_values_am3, y_values_am3):
    print(f"x = {x:.2f}, y = {y:.6f}")




# Vẽ đồ thị so sánh
plt.figure(figsize=(12, 6))

# Đồ thị so sánh giữa RK4 và Adams-Bashforth 3
plt.subplot(1, 2, 1)
plt.plot(x_values_rk4, y_values_rk4, label='RK4', color='blue')
plt.plot(x_values_ab3, y_values_ab3, label='AB3', color='green', linestyle='--')
plt.title('So sánh RK4 và Adams-Bashforth 3 (AB3)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Đồ thị so sánh giữa RK4 và Adams-Moulton 3
plt.subplot(1, 2, 2)
plt.plot(x_values_rk4- x_values_am3, y_values_rk4- y_values_am3, label='Rk4-AM3', color='red', linestyle='--')
plt.title('So sánh RK4 và Adams-Moulton 3 (AM3)')
plt.xlabel('Delta x')
plt.ylabel('Delta y')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
