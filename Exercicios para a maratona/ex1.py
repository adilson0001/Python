# Crie uma função recursiva que receba um número inteiro não negativo n e retorne o fatorial de n

def fatorial(num):
    if num==0:
        return 1
    else:
        return num*fatorial(num-1)

valor=int(input())
print(fatorial(valor))
