import numpy as np
import matplotlib as plt
import matplotlib.pyplot # Carrega o módulo necessário internamente

# Definindo os vetores
v1 = np.array([4, 3])
v2 = np.array([-2, 5])
v3 = np.array([1, -2])
v_soma = v1 + v2 + v3

# Configuração do gráfico
# Agora o plt.pyplot vai funcionar porque carregamos ele acima
origin = np.array([[0, 0, 0], [0, 0, 0]]) 

plt.pyplot.figure(figsize=(7, 5))

# Plotando os vetores: quiver(origem_x, origem_y, destino_x, destino_y)
plt.pyplot.quiver(*origin, [v1[0], v2[0], v_soma[0]], [v1[1], v2[1], v_soma[1]], 
           color=['r', 'b', 'g'], scale=1, scale_units='xy', angles='xy', 
           label=['V1 (4,3)', 'V2 (-2,5)', 'Soma (3,6)'])

# Ajustes de visualização
plt.pyplot.xlim(-4, 7)
plt.pyplot.ylim(-4, 7)
plt.pyplot.axhline(0, color='black', linewidth=1) 
plt.pyplot.axvline(0, color='black', linewidth=1) 
plt.pyplot.grid(True, linestyle=':')
plt.pyplot.legend()
plt.pyplot.title("Soma de Vetores: V1 + V2")

plt.pyplot.show()