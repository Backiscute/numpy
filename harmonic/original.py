# French

import numpy as np
import matplotlib.pyplot as plt

# Voltage
E=10
# Resistance
r=5
# Inductance
L=0.1
# Fréquence
f=50
omega=2*np.pi*f
# Periode
T=1/f
# Temps
t=np.linspace(0,3*T,1000)
phi_1=-np.arctan((L*omega)/r)
terme_continue=E/(np.pi*r)
terme_fondamental=(E/(2*np.sqrt(r**2+(L*omega)**2)))*np.cos(omega*t-np.pi/2+phi_1)
N=1000000
somme_harmonique=np.zeros_like(t)
for p in range(1,N):
    omega_p=2*p*omega
    phi_p=-np.arctan((L*omega_p)/r)
    num=np.cos(2*p*omega*t+phi_p)
    denum=np.sqrt(r**2+(L*omega_p)**2)*(1-4*(p**2))
    terme_somme = num/denum
    somme_harmonique+= (2*E)/np.pi* terme_somme

i = terme_fondamental + terme_continue + somme_harmonique

plt.figure(figsize=(E, r))
plt.plot(t, terme_continue * np.ones_like(t), label='Terme continue', color='black', linestyle='--', linewidth=2)
plt.plot(t, terme_fondamental, label='Terme fondamental', color='r', linewidth=2)
plt.plot(t, somme_harmonique, label='Somme Harmonique', color='black', linewidth=2)
plt.plot(t, i, label='$i(t)$', color='b', linewidth=2)
plt.title('Trace du courant total $i(t)$ dans le circuit')
plt.xlabel('Temps $t$ (s)')
plt.ylabel('$i(t)$ (A)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.show()