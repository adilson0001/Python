# Crie uma função recursiva que calcule baseexpoente, recebendo dois inteiros: base e expoente.


def potencia(base, expoente):
    if expoente == 0:
        return 1
    if expoente < 0:
        return 1 / potencia(base, -expoente)
    return base * potencia(base, expoente - 1)

