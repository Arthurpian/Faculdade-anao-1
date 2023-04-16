numero_da_tabuada = input("Digite o número que quer saber a tabuada: ")
while not numero_da_tabuada.isnumeric():
    numero_da_tabuada = input("Digite um número valido: ")

numero_da_tabuada = int(numero_da_tabuada)

i = 1

while i != 11:
    print(f"{numero_da_tabuada} x {i} = {i*numero_da_tabuada}")
    i+=1
