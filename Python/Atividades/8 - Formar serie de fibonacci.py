quantidade = input("Digite quantos números você quer ver da Fibonacci: ")
while not quantidade.isnumeric():
    quantidade = input("Digite um número valido: ")

quantidade = int(quantidade)

i = 0
num_1 = 1
num_2 = 1
num_3 = 0

print(num_1)
print(num_2)

quantidade -= 2

while i < quantidade:
    num_3 = num_2 + num_1
    print(num_3)
    num_2 = num_1
    num_1 = num_3
    i += 1