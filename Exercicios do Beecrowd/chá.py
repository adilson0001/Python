cha=int(input())

respostas=input() 

c1,c2,c3,c4,c5=respostas.split()

c1=int(c1)
c2=int(c2)
c3=int(c3)
c4=int(c4)
c5=int(c5)
correto=0

if c1==cha:
    correto+=1
if c2==cha:
    correto+=1
    
if c3==cha:
    correto+=1
    
if c4==cha:
    correto+=1

if c5==cha:
    correto+=1
print(correto)
        