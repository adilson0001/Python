class Aluno:

    def estudar(self):
        print("Estudando...")

    def fazer_prova(self, materia):
        print(f"Fazendo prova de {materia}")

    def media_padrao(self):
        return 7

    def calcular_media(self, n1, n2):
        return (n1 + n2) / 2

aluno1 = Aluno()

aluno1.estudar()

aluno1.fazer_prova("Matemática")

print(aluno1.media_padrao())

print(aluno1.calcular_media(8, 6))


