idade=int(input())

ano=0
meses=0
dias=0
if idade>=365:
    ano=idade/365
    meses=idade%365
    dias=meses%30

else:
    meses=idade%365
    dias=meses%30
   
print(f"{ano:} ano (s)")
print(f"{meses} mes (es)")
print(f"{dias} dia (s)")
    
    

     
          
           
         
          
        
    
 