nome = input("Digie seu nome: ")
while len(nome) <= 3:
    nome = input("Digie seu nome: ")

idade = input("Digie sua idade: ")
while not idade.isnumeric():
    idade = input("Digite sua idade (ex: 18):")

salario = input("Digite seu salario: ")
while not salario.isnumeric():
    salario = input("Digite so numeros: ")

sexo = input("Qual e seu sexo (f= feminino ou m = masculino): ")
while sexo != "f" and sexo != "m":
    sexo = input("f ou m")

estado_civil = input("Digite seu estado civil s = solteiro , c = casado , v = vivo ou d = damasco: ")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Digite seu estado civil s = solteiro , c = casado , v = vivo ou d = damasco: ")

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)
