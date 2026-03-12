

notas=[]

for x in range(2):
    codigo_aluno=input("RM: ")
    nota=float(input("nota: "))
    resultado=[codigo_aluno, nota]
    notas.append(resultado)


print( "quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("o RM", codigo_aluno, "tirou a nota", nota)