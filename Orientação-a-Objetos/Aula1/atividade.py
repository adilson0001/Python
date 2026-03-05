#Criar:
#Classe: CalculadoraFinanceira
#
#Métodos:
#mostrar_boas_vindas() → imprime mensagem
#calcular_juros(valor, taxa) → retorna valor * taxa / 100
#calcular_total(valor, taxa) → retorna valor + juros
#dobrar_valor(valor) → retorna valor * 2

class CalculadoraFinanceira:

    # Sem parâmetro e sem retorno
    def mostrar_boas_vindas(self):
        print("Bem-vindo à calculadora financeira.")

    # Com parâmetros e com retorno
    def calcular_juros(self, valor, taxa):
        return valor * taxa / 100

    # Com parâmetros e com retorno
    def calcular_total(self, valor, taxa):
        juros = self.calcular_juros(valor, taxa)
        return valor + juros

    # Com parâmetro e com retorno
    def dobrar_valor(self, valor):
        return valor * 2


calc = CalculadoraFinanceira()

calc.mostrar_boas_vindas()

print("Juros:", calc.calcular_juros(1000, 10))

print("Total com juros:", calc.calcular_total(1000, 10))

print("Valor dobrado:", calc.dobrar_valor(1000))