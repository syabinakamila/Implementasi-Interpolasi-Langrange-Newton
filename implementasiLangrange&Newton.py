import numpy as np
import matplotlib.pyplot as plt

# Data 
tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x, x_data, y_data):
    n = len(x_data)
    result = 0.0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    coefficients = np.zeros(n)
    coefficients[0] = y_data[0]
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            y_data[j] = (y_data[j] - y_data[j-1]) / (x_data[j] - x_data[j-i])
        coefficients[i] = y_data[i]
    
    result = 0.0
    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_data[j])
        result += term
    return result

def plot_interpolation(x_values, y_values_lagrange, y_values_newton):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values_lagrange, label='Polinomial Lagrange')
    plt.plot(x_values, y_values_newton, label='Polinomial Newton')
    plt.scatter(tegangan, waktu_patah, color='red', label='Data Asli')
    plt.xlabel('Tegangan (kg/mm²)')
    plt.ylabel('Waktu Patah (jam)')
    plt.title('Interpolasi Polinomial Langrange & Newton')
    plt.legend()
    plt.grid(True)
    plt.show()

# Data u/ plotting
x_values = np.linspace(5, 40, 100)
y_values_lagrange = [lagrange_interpolation(x, tegangan, waktu_patah) for x in x_values]
y_values_newton = [newton_interpolation(x, tegangan, waktu_patah) for x in x_values]

# Plot hasil interpolasi
plot_interpolation(x_values, y_values_lagrange, y_values_newton)

# Pengujian u/ rentang 5 <= x <= 40
x_test_range = np.linspace(5, 40, 100)
y_lagrange_range = [lagrange_interpolation(x, tegangan, waktu_patah) for x in x_test_range]
y_newton_range = [newton_interpolation(x, tegangan, waktu_patah) for x in x_test_range]

# Plot hasil interpolasi untuk rentang 5 <= x <= 40
plot_interpolation(x_test_range, y_lagrange_range, y_newton_range)

# Pengujian dgn contoh data
x_test = 25
y_lagrange = lagrange_interpolation(x_test, tegangan, waktu_patah)
y_newton = newton_interpolation(x_test, tegangan, waktu_patah)

print("Hasil interpolasi Polinomial Lagrange untuk x =", x_test, ":", y_lagrange)
print("Hasil interpolasi Polinomial Newton untuk x =", x_test, ":", y_newton)
