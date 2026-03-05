#Na classe Produto, crie um novo método chamado:
#aplicar_desconto(porcentagem)
#
#O método deve reduzir o preço do produto.
#
#No programa principal:
#crie um objeto da classe Produto
#aplique um desconto
#mostre o preço antes e depois do desconto.



class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_produto(self):
        print("\nProduto:", self.nome)
        print("Preço:", self.preco)

    def calcular_total(self):
        return self.preco * self.quantidade
    
    def aplicar_desconto(self,porcentagem):
        print("\nAntes do Desconto:\n")
        print("Produto:", self.nome)
        print("Preço:", self.preco)
        print("Depois do Desconto:\n")
        print("Produto:", self.nome)
        print("Preço:", porcentagem/100*self.preco)

produto1 = Produto("Mouse",50,3)
produto1.mostrar_produto()
desconto=int(input("\nDigite a porcentagem de desconto unitario. ex(15): "))
produto1.aplicar_desconto(desconto)



