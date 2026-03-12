
matriz=[]  


for i in range(8):
    matriz.append([1,0,0,0,0,0,0,0])

for u in range(1):
    for o in range(8):     
        if o==8:
            matriz[1][o]=1
        


for l in matriz:  
    for u in l:  
        print(u, end="  ")
    print()
  

