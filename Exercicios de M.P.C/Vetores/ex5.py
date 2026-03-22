import numpy as np
import matplotlib.pyplot as plt

# 1. Definição dos vetores
u = np.array([3, 1])
v = np.array([4, 2])

# 2. Cálculos Matemáticos
# Produto Escalar
produto_escalar = np.dot(u, v)

# Normas (comprimentos)
norma_u = np.linalg.norm(u)
norma_v = np.linalg.norm(v)

# Cosseno de teta (u.v / |u||v|)
cos_teta = produto_escalar / (norma_u * norma_v)

# Ângulo em radianos e graus
teta_rad = np.arccos(np.clip(cos_teta, -1.0, 1.0)) # clip evita erros numéricos
teta_graus = np.degrees(teta_rad)

# 3. Exibição dos resultados
print(f"--- Resultados dos Cálculos ---")
print(f"Produto Escalar: {produto_escalar}")
print(f"Norma de u: {norma_u:.4f}")
print(f"Norma de v: {norma_v:.4f}")
print(f"Cosseno de teta: {cos_teta:.4f}")
print(f"Ângulo entre os vetores: {teta_graus:.2f}°")

# 4. Visualização Gráfica
plt.figure(figsize=(8, 8))
origin = np.array([0, 0])

# Plotagem dos vetores
plt.quiver(0, 0, u[0], u[1], color='r', angles='xy', scale_units='xy', scale=1, label=f'u {u}')
plt.quiver(0, 0, v[0], v[1], color='b', angles='xy', scale_units='xy', scale=1, label=f'v {v}')

# Ajustes do gráfico
limite = max(np.max(u), np.max(v)) + 1
plt.xlim(-1, limite)
plt.ylim(-1, limite)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title(f"Visualização de Vetores\nÂngulo aproximado: {teta_graus:.2f}°")

plt.show()