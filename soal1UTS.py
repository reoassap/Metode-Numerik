import math
import matplotlib.pyplot as plt

# Soal 1a - Fungsi untuk menghitung f(R) dan f'(R)
def f(R, L=0.5, C=10e-6):
    try:
        result = (1 / (2 * math.pi)) * math.sqrt((1 / (L * C)) - (R ** 2 / (4 * L ** 2)))
        return result
    except ValueError:
        # Mengembalikan None jika terjadi kesalahan akar negatif
        return None

def df_dR(R, L=0.5, C=10e-6):
    try:
        result = -R / (4 * math.pi * L ** 2 * math.sqrt((1 / (L * C)) - (R ** 2 / (4 * L ** 2))))
        return result
    except ValueError:
        # Mengembalikan None jika terjadi kesalahan akar negatif
        return None

# Soal 1b - Metode Biseksi
def bisection_method(func, target, a, b, tolerance=0.1):
    if func(a) * func(b) > 0:
        raise ValueError("Fungsi tidak berubah tanda pada interval yang diberikan.")
    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        midpoint_value = func(midpoint)
        
        if midpoint_value is None:
            raise ValueError("Fungsi menghasilkan nilai None dalam interval ini.")
        
        if midpoint_value == target:
            return midpoint
        elif func(a) * midpoint_value < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

# Implementasi metode biseksi
target_f = 1000  # Frekuensi yang diinginkan
resonance_func = lambda R: f(R) - target_f  # Fungsi untuk menemukan R pada target frekuensi
try:
    R_bisection = bisection_method(resonance_func, target_f, 0, 100)
except ValueError as e:
    print("Error pada metode Biseksi:", e)

# Soal 1c - Metode Newton-Raphson
def newton_raphson(func, d_func, x0, tolerance=0.1, max_iter=100):
    x = x0
    for _ in range(max_iter):
        func_value = func(x)
        d_func_value = d_func(x)
        
        if d_func_value is None or d_func_value == 0:
            raise ValueError("Turunan fungsi menghasilkan nilai None atau nol.")
        
        x_new = x - func_value / d_func_value
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

# Implementasi metode Newton-Raphson
try:
    R_newton = newton_raphson(resonance_func, df_dR, 50)
except ValueError as e:
    print("Error pada metode Newton-Raphson:", e)

# Soal 1d - Membandingkan hasil dan kecepatan konvergensi
if 'R_bisection' in locals():
    print(f"Hasil Biseksi: R = {R_bisection}")
if 'R_newton' in locals():
    print(f"Hasil Newton-Raphson: R = {R_newton}")

# Visualisasi hasil tanpa NumPy
R_values = [i * 0.1 for i in range(1001)]
f_values = [f(R) for R in R_values if f(R) is not None]
R_values = [R for R in R_values if f(R) is not None]
plt.plot(R_values, f_values, label='Frekuensi Resonansi')
plt.axhline(y=target_f, color='r', linestyle='--', label='Target 1000 Hz')
if 'R_bisection' in locals():
    plt.scatter([R_bisection], [target_f], color='g', marker='o', label='Hasil Biseksi')
if 'R_newton' in locals():
    plt.scatter([R_newton], [target_f], color='b', marker='x', label='Hasil Newton-Raphson')
plt.xlabel('R (Ohm)')
plt.ylabel('Frekuensi (Hz)')
plt.legend()
plt.show()
