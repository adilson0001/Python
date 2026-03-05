class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def maior_menor(self,idade):
        if self.idade>=18:
            print("Maior de idade")
        else:
            print("Menor de idade")

    def apresentar(self):
        print("Aluno:", self.nome)
        print("Curso:", self.curso)

    def calcular_media(self, n1, n2):
        return (n1 + n2) / 2


aluno1 = Aluno("Maria", 17, "DS")
aluno1.maior_menor(aluno1.idade)
aluno1.apresentar()
print("Média:", aluno1.calcular_media(8, 7))