# Crie um programa que:

# Leia uma matriz 3x3 (números inteiros digitados pelo usuário).

# Mostre a matriz formatada (em forma de tabela).

# Calcule a soma de todos os elementos da matriz.

# Mostre a soma apenas dos elementos da diagonal principal.

# Exemplo de entrada:
# Digite o número da posição [0,0]: 1
# Digite o número da posição [0,1]: 2
# Digite o número da posição [0,2]: 3
# Digite o número da posição [1,0]: 4
# Digite o número da posição [1,1]: 5
# Digite o número da posição [1,2]: 6
# Digite o número da posição [2,0]: 7
# Digite o número da posição [2,1]: 8
# Digite o número da posição [2,2]: 9

# Saída esperada:
# Matriz:
# 1  2  3
# 4  5  6
# 7  8  9

# Soma de todos os elementos = 45
# Soma da diagonal principal = 15



matriz=[]

# cria a matriz com zeros
for i in range(3):
    linha=[]
    for u in range(3):        
        linha.append(int((input(f"Digite o número da posição [{i}] [{u}]: "))))
    matriz.append(linha)

resu=0

for Linha in matriz:
    for Coluna in Linha:
       resu+=Coluna
soma=0
for linhA in range(3):
    for colunA in range(3):
        if linhA==colunA:
            soma+=matriz[linhA][colunA]
   
# printa as matrizes
print("Matriz:")     
for LInha in matriz:
    for elemento in LInha:
        print(elemento, end="  ")
    print()

print(f"Soma dos elementos = {resu}")
print(f"Soma da diagonal principal = {soma}")
