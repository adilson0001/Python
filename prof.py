from Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome, snome, email, tel, salario):
        super().__init__(nome, snome, email, tel)
        self.salario = salario

    def ExibirTipoSalario(self):
        if self.salario > 4000:
            return "Salário acima da média"
        else:
            return "Salário abaixo da média"


prof1 = Professor(
    nome="Maria",
    snome="Santos",
    email="maria123@gmail.com",
    tel="11 7878-5858",
    salario=5200
)

print(prof1.ExibirNome_Completo())
print(prof1.ExibirTipoSalario())