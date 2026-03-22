import matplotlib.pyplot as plt
import numpy as np

# Definição dos vetores
A = np.array([12, -3])
B = np.array([5, 2])
v_sub = A * B  # Resultado: [60, -6]

# Origens para cada vetor (todos partindo de 0,0)
origin = np.array([[0, 0, 0], [0, 0, 0]]) 

plt.figure(figsize=(8, 6))

# O quiver recebe: origem_x, origem_y, componentes_x, componentes_y
plt.quiver(*origin, 
           [A[0], B[0], v_sub[0]], 
           [A[1], B[1], v_sub[1]], 
           color=['r', 'b', 'g'], 
           scale=1, scale_units='xy', angles='xy')

# Criando legendas manuais para evitar erros com o quiver
plt.plot([], [], color='r', label=f'A {A}')
plt.plot([], [], color='b', label=f'B {B}')
plt.plot([], [], color='g', label=f'A - B {v_sub}')

# Ajustes de visualização para que todos os vetores apareçam
plt.xlim(-2, 74)
plt.ylim(-7, 4)

plt.axhline(0, color='black', linewidth=1) 
plt.axvline(0, color='black', linewidth=1) 
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Subtração de Vetores: A - B")

plt.show()