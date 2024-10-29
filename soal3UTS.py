import math
import matplotlib.pyplot as plt

# Soal 3a - Metode Selisih Maju, Mundur, dan Tengah
def R(T):
    return 5000 * math.exp(3500 * (1 / T - 1 / 298))

def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Soal 3b - Metode Eksak
def exact_derivative_R(T):
    return -5000 * 3500 * math.exp(3500 * (1 / T - 1 / 298)) / T ** 2

# Menghitung dan menampilkan hasil
T_values = list(range(250, 351, 10))  # Range dari 250K sampai 350K dengan interval 10K
forward_diff = [forward_difference(R, T) for T in T_values]
backward_diff = [backward_difference(R, T) for T in T_values]
central_diff = [central_difference(R, T) for T in T_values]
exact_diff = [exact_derivative_R(T) for T in T_values]

# Soal 3d - Plot Error Relatif
plt.plot(T_values, forward_diff, label='Selisih Maju')
plt.plot(T_values, backward_diff, label='Selisih Mundur')
plt.plot(T_values, central_diff, label='Selisih Tengah')
plt.plot(T_values, exact_diff, label='Eksak', linestyle='--')
plt.xlabel('Temperatur (K)')
plt.ylabel('dR/dT')
plt.legend()
plt.show()
