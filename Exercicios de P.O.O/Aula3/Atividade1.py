# PARTE 1
class Veiculo:
    def __init__(self, marca,modelo,ano):        
        self.marca=marca
        self.modelo=modelo
        self.ano=ano

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano de Fabricação: {self.ano}")

    def verificar_idade(self, ano_atual):
        idade = ano_atual - self.ano  # Cálculo da idade real
        
        if idade <= 3:
            print(f"O Veiculo tem {idade} anos e é Novo")
        elif 4 <= idade <= 10:
            print(f"O Veiculo tem {idade} anos e é Seminovo")
        else:
            print(f"O Veiculo tem {idade} anos e é Antigo")





# PARTE 2

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, n_portas, t_combustivel):
        super().__init__(marca, modelo, ano)
        self.n_portas=n_portas
        self.t_combustivel=t_combustivel

    def info_carro(self):
        super().exibir_dados()
        print(f"Numero de Portas: {self.n_portas}")
        print(f"Tipo do Combustivel: {self.t_combustivel}")



# parte 3
      
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, tipo_partida):
        super().__init__(marca, modelo, ano)
        self.cilindradas=cilindradas
        self.tipo_partida=tipo_partida

    def info_moto(self):
        super().exibir_dados()
        print(f"Numero de Cilindradas: {self.cilindradas}")
        print(f"Tipo de Partida: {self.tipo_partida}")





#  PARTE 4

carro = Carro("Toyota", "Corolla", 2020, 4,"Diesel")
moto = Moto("Honda","CG 160", 1920, 160, "Eletrica")

print("\nCarro")
carro.info_carro()

print("\nMoto")
moto.info_moto()