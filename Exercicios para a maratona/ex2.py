# Crie uma função recursiva que receba um vetor/lista de números e retorne a soma de todos os seus
# # elementos, sem usar laços de repetição.

def soma_vetor(lista):
    if not lista:
        return 0
    return lista[0] + soma_vetor(lista[1:])

entrada = input("Digite os números separados por espaço: ")

numeros = list(map(int, entrada.split()))

resultado = soma_vetor(numeros)
print(f"A soma dos elementos é: {resultado}")