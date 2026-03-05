'''é melhor contar cada um dos dois primeiros anos humanos como 10,5 anos de cão 
e, depois, contar cada ano humano adicional como 4 anos de cão.

Escreva um programa que pergunte a idade do usuário e implemente a conversão de 
anos humanos para anos de cachorro descritos no parágrafo anterior. Você deverá 
mostrar na tela a idade digitada e, em seguida, a mensagem “Se você fosse um cão, 
teria X anos”.
Verifique se o seu programa funciona corretamente para conversões inferiores a dois 
anos humanos e para conversões de dois ou mais anos humanos. 

Seu programa deve 
exibir uma mensagem de erro apropriada se o usuário digitar um número negativo ou 
zero para a sua idade'''


import sys

try:
    
    idade= int(input("digite a sua idade: "))

except ValueError:
    print("voce não digitou uma idade valida!")
    sys.exit()

if idade<=0:

    sys.exit("voce não digitou uma idade valida!")
    

if idade>=2 :
    idade=(idade-2)
    idade=idade*4
    idade=idade+(2*10.5)
    
elif idade==1: 
   
    idade=idade*10.5


print(f"Se você fosse um cão,teria {idade} anos")


    



