import numpy as np
import matplotlib.pyplot as plt

# vitesse initiale (m/s)
v0 = 20
# gravité (m/s²)
g = 9.81
# hauteur initiale (m)
y0 = 0
# angles de tir (degrés)
angles = [20, 35, 60, 40, 50, 70]

for alpha in angles:
    # conversion en radians
    a = np.radians(alpha)
    # instant final
    tf = 2 * v0 * np.sin(a) / g
    # interval de temps
    t = np.linspace(0, tf, 100)
    # équations horaires
    x = v0 * np.cos(a) * t
    y = y0 + v0 * np.sin(a) * t - 0.5 * g * t ** 2
    
    print(f"--- Angle: {alpha}° ---")
    print("Radians:", round(a, 2))
    print("Duree du vol:", round(tf, 2), "s")
    print("Portee:", round(x[-1], 2), "m")
    print("Hauteur maximale:", round(max(y), 2), "m")
    
    plt.plot(x, y, label=f"{alpha}°")
    
plt.xlabel("Distance horizontale (m)")
plt.ylabel("Hauteur (m)")
plt.title("Trajectoire d'un ballon de football")
plt.grid()
plt.legend()
plt.show()