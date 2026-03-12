def frete(quantidade):
    if quantidade>1:
        quantidade=quantidade-1
        quantidade=quantidade*2.95
        quantidade=quantidade+10.95
    else:
        quantidade=10.95
    
    return quantidade

itens = int(input("digite a quantidade de itens comprados: "))
print(f"quantidade de itens: {itens}, valor de frete: {frete(itens):.2f}")

