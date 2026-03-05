def bandeira1(km):
    tarifa = 4.5
    valor_km = km * 2.75
    return tarifa + valor_km

def bandeira2(km):
    tarifa = 5.85
    valor_km = km * 3.5
    return tarifa + valor_km

# Entrada do usuário
dia = int(input("Digite o dia da semana (1=Segunda, ..., 7=Domingo): "))
horario = float(input("Digite o horário (formato 24h, ex: 13.5 para 13h30): "))
km = float(input("Digite os quilômetros percorridos: "))

# Validação do dia
if not 1 <= dia <= 7:
    print("Você não digitou um dia válido.")
else:
    if dia == 7:
        # Domingo: bandeira 2 o dia todo
        total = bandeira2(km)
        print(f"Bandeira 2 (domingo). Valor da corrida: R$ {total:.2f}")
    elif 6 <= horario < 20:
        # Segunda a sábado das 6h até antes das 20h → bandeira 1
        total = bandeira1(km)
        print(f"Bandeira 1. Valor da corrida: R$ {total:.2f}")
    else:
        # Segunda a sábado das 20h às 6h → bandeira 2
        total = bandeira2(km)
        print(f"Bandeira 2. Valor da corrida: R$ {total:.2f}")