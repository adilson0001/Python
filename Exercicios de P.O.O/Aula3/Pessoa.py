class Pessoa:
    def __init__(self, nome, snome, email, tel):
        self.nome = nome
        self.snome = snome
        self.email = email
        self.tel = tel

    def ExibirNome_Completo(self):
        return "Nome Completo: " + self.nome + " " + self.snome


# Objeto 1
p1 = Pessoa(
    nome="Maria",
    snome="Santos",
    email="maria123@gmail.com",
    tel="11 7878-5858"
)

# Objeto 2
p2 = Pessoa(
    nome="José",
    snome="Ferreira",
    email="jose@email.com",
    tel="11 9999-1234"
)

print(p1.ExibirNome_Completo())
print(p2.ExibirNome_Completo())