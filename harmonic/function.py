import numpy as np
import matplotlib.pyplot as plt

# Voltage
E = 10
resistance = 5
# Inductance
L = 0.1
frequency = 50
# Angular frequency
omega = 2 * np.pi * frequency
# Period
T = 1 / frequency
# Time
t = np.linspace(0, 3 * T, 1000)

phi_1 = -np.arctan((L * omega) / resistance)
dc_term = E / (np.pi * resistance)
fundamental_term = (E / (2 * np.sqrt(resistance**2 + (L * omega) ** 2))) * np.cos(omega * t - np.pi / 2 + phi_1)

harmonic_sum = np.zeros_like(t)
# We use a high number of harmonics to approximate the series, but we can limit it to a reasonable number for performance
# As this function converges quickly, we can use a smaller number of harmonics for practical purposes as 50
N = 1000000
for p in range(1, N):
    omega_p = 2 * p * omega
    phi_p = -np.arctan((L * omega_p) / resistance)
    numerator = np.cos(2 * p * omega * t + phi_p)
    denominator = np.sqrt(resistance ** 2 + (L * omega_p) ** 2) * (1 - 4 * (p ** 2))
    sum_term = numerator / denominator
    harmonic_sum += (2 * E) / np.pi * sum_term

i = fundamental_term + dc_term + harmonic_sum

plt.figure(figsize=(E, resistance))
plt.plot(t, dc_term * np.ones_like(t), label='DC term', color='black', linestyle='--', linewidth=2)
plt.plot(t, fundamental_term, label='Fundamental term', color='r', linewidth=2)
plt.plot(t, harmonic_sum, label='Harmonic sum', color='black', linewidth=2)
plt.plot(t, i, label='$i(t)$', color='b', linewidth=2)
plt.title('Plot of the total current $i(t)$ in the circuit')
plt.xlabel('Time $t$ (s)')
plt.ylabel('$i(t)$ (A)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.show()