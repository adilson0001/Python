# Crie uma função recursiva que receba um número inteiro positivo n e imprima os valores de n até
# 0

def contagem(n):
    if n==0:
        print(0)

    else:
        print(f"{n}")
        contagem(n-1)
        


v=int(input())

contagem(v)