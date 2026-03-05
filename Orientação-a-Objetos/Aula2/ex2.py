class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_produto(self):
        print("Produto:", self.nome)
        print("Preço:", self.preco)

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Mouse",50,3)
produto1.mostrar_produto()
print(f"Total investido em estoque: {produto1.calcular_total()}")




