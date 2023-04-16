cidade_alem = 80000
cidade_Belem = 200000
i=0

while cidade_alem < cidade_Belem:

    cidade_Belem = ((cidade_Belem * 1.5) / 100) + cidade_Belem
    cidade_alem = ((cidade_alem * 3) / 100) + cidade_alem
    i+=1

print(i)