import numpy as np

# 1. Captura os valores e já cria o vetor em uma linha
u = np.array([float(input("ux: ")), float(input("uy: "))])
v = np.array([float(input("vx: ")), float(input("vy: "))])

# 2. Calcula o produto escalar
# Se o produto for 0, o Python entende como "False" no if, 
# por isso verificamos se é igual a zero.
if np.dot(u, v) == 0:
    print("Força aplicada de forma eficiente")
else:
    print("Força desalinhada com a superfície")