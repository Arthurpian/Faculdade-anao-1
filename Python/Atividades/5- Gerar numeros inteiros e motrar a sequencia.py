#Meu codigo
num_1 = input("Me diga um número: ")
while not num_1.isnumeric():
    num_1 = input("Me diga um numero valido: ")

num_2 = input("Me diga outro número: ")
while not num_2.isnumeric():
    num_2 = input("Me diga um número valido: ")

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1)

if num_1 < num_2:
    while num_1 < num_2:
        num_1 = num_1 + 1
        print(num_1)

else:
    while num_2 != num_1:
        num_1 = num_1 - 1
        print(num_1)

# Codigo do professor
""""
num1 = int(input("Diga um número: "))
num2 = int(input("Diga um número: "))
menor = num1
maior = num2
if num2<num1:
    menor = num2
    maior = num1
while menor<=maior:
    print(menor)
    menor+=1
"""