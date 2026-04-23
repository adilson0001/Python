import matplotlib.pyplot as plt
import numpy as np

# Definição dos vetores
u = np.array([3, 2])
v = np.array([1, 1])
w = np.array([5, 1])

# Coeficientes encontrados
a, b = 4, -7

# Componentes da combinação linear
au = a * u
bv = b * v

plt.figure(figsize=(10, 8))

# Vetores principais (partindo da origem)
plt.quiver(0, 0, u[0], u[1], color='r', angles='xy', scale_units='xy', scale=1, label='u (3,2)')
plt.quiver(0, 0, v[0], v[1], color='b', angles='xy', scale_units='xy', scale=1, label='v (1,1)')
plt.quiver(0, 0, w[0], w[1], color='black', angles='xy', scale_units='xy', scale=1, width=0.015, label='w (5,1) resultante')

# Visualização da combinação linear (Regra do polígono)
# Plotamos au e depois bv partindo da ponta de au
plt.quiver(0, 0, au[0], au[1], color='r', alpha=0.3, angles='xy', scale_units='xy', scale=1, label='4u')
plt.quiver(au[0], au[1], bv[0], bv[1], color='b', alpha=0.3, angles='xy', scale_units='xy', scale=1, label='-7v (a partir de 4u)')

# Ajustes de layout
plt.xlim(-2, 13)
plt.ylim(-8, 9)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.title(f"Combinação Linear: w = {a}u + ({b})v")

plt.show()