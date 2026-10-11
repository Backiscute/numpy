import numpy as np
import matplotlib.pyplot as plt

# initial velocity (m/s)
v0 = 20
# gravity (m/s²)
g = 9.81
# initial height (m)
y0 = 0
# launch angles (degrees)
angles = [20, 35, 60, 40, 50, 70]

for alpha in angles:
    # convert to radians
    a = np.radians(alpha)
    # final time (time of flight)
    tf = 2 * v0 * np.sin(a) / g
    # time interval
    t = np.linspace(0, tf, 100)
    # equations of motion
    x = v0 * np.cos(a) * t
    y = y0 + v0 * np.sin(a) * t - 0.5 * g * t ** 2
    
    print(f"--- Angle: {alpha}° ---")
    print("Radians:", round(a, 2))
    print("Flight time:", round(tf, 2), "s")
    print("Range:", round(x[-1], 2), "m")
    print("Maximum height:", round(max(y), 2), "m")
    
    plt.plot(x, y, label=f"{alpha}°")
    
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Trajectory of a football")
plt.grid()
plt.legend()
plt.show()