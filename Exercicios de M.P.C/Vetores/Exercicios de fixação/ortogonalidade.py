

import numpy as np

ux=int(input("Digite o componente x do vetor u: "))
uy=int(input("Digite o componente y do vetor u: "))

vx=int(input("Digite o componente x do vetor v: "))
vy=int(input("Digite o componente y do vetor v: "))

u=np.array([ux,uy])
v=np.array([vx,vy])
produto_escalar=np.dot(u,v)
norma_u=np.linalg.norm(u)
norma_v=np.linalg.norm(v)

if produto_escalar == 0:
    print("Os vetores u e v são ortogonais.")
else:
    print("Os vetores u e v não são ortogonais.")