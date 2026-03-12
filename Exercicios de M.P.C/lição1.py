

'biblioteca para calcular raiz'
import math

'pitoresco = pitagoras'
def pitoresco(l1,l2):
    A= (l1**2)+(l2**2)
    return math.sqrt(A)

'lados pega os valores dos catetos'   
Lados = input("digite os dois comprimentos dos lados mais curtos de um triângulo retângulo: ")

'separa os catetos e converte pra int'
l1,l2 = map(int, Lados.split())


print(f"se os catetos tem o valor de: {Lados} a hipotenusa será de: {pitoresco(l1,l2):.2f}")
