from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, snome, email, tel, n_matricula, curso):
        super().__init__(nome, snome, email, tel)
        self.n_matricula = n_matricula
        self.curso = curso
    def NomeCompleto(self):
        super().ExibirNome_Completo()
        print(f"Numero de matricula: {self.n_matricula}")



aluno1=Aluno("Jose",
    "da Silva",
    "silvinha@gmail.com",
    "40028922",
    "77777",
    "DSM")

print(aluno1.NomeCompleto())







