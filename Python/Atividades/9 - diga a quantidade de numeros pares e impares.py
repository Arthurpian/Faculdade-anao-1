i = 0
par = 0
impar = 0

while i < 10:
    num = input("Digite um número: ")
    while not num.isnumeric():
        num = input("Digite um número valido: ")

    num = int(num)

    if num % 2:
        impar += 1
    else:
        par += 1

    i+=1

print(f"Você digitou {par} números pares é {impar} números impares.")