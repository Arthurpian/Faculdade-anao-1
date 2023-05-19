def input_numerico(msg,j):
    num = input(msg)
    i = j
    while not num.isnumeric():
        print(f"Voce tem mais {i} tentativas")
        print("Tem que ser número")
        num = input(msg)
        i-=1

    if i == 0:
        print("Tentativas excedidas")
        return
    return num

garrafas = input_numerico("Diga a qtd de garrafas: ", 2)
print(garrafas)
