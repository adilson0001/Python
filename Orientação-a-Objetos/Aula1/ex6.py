class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    # Sem parâmetro e sem retorno
    def mostrar_mensagem(self):
        print("Bem-vindo ao sistema bancário.")

    # Com parâmetro e sem retorno
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado.")

    # Sem parâmetro e com retorno
    def consultar_saldo(self):
        return self.saldo

    # Com parâmetro e com retorno
    def calcular_rendimento(self, taxa):
        return self.saldo * (taxa / 100)
    
conta1 = ContaBancaria(1000)

conta1.mostrar_mensagem()

conta1.depositar(500)

print("Saldo atual:", conta1.consultar_saldo())

print("Rendimento com 10%:", conta1.calcular_rendimento(10))
