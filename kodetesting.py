# Pengujian  rentang 5 <= x <= 40
x_test_range = np.linspace(5, 40, 100)
y_lagrange_range = [lagrange_interpolation(x, tegangan, waktu_patah) for x in x_test_range]
y_newton_range = [newton_interpolation(x, tegangan, waktu_patah) for x in x_test_range]

# Plot hasil interpolasi  rentang 5 <= x <= 40
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_lagrange, label='Polinomial Lagrange')
plt.plot(x_values, y_values_newton, label='Polinomial Newton')
plt.scatter(tegangan, waktu_patah, color='red', label='Data Asli')
plt.plot(x_test_range, y_lagrange_range, linestyle='--', label='Interpolasi Lagrange (5 <= x <= 40)')
plt.plot(x_test_range, y_newton_range, linestyle='--', label='Interpolasi Newton (5 <= x <= 40)')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinomial Langrange & Newton')
plt.legend()
plt.grid(True)
plt.show()