
'''se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)

se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.
Sua tarefa é escrever uma calculadora de impostos.'''



num = float(input("digite sua renda: "))

if num <=85528:
    tax=(num*0.18)-556.2
    

   
elif num>85528:
    tax=(num-85528)*0.32+14839.2
    
if tax<0:
    tax=0
    
print("a taxa é de: ",round(tax,0), "thalers")