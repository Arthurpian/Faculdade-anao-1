i = 0
soma = 0

while i < 5:
    nota = input("Me diga sua nota: ")
    while not nota.isnumeric():
        nota = input("Digite um numero valido: ")
    nota = int(nota)
    soma += nota
    i+=1

print(f"A soma das notas é {soma} é a média é {soma/5}")