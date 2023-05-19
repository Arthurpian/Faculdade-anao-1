def maior(lista):
    j = 0
    for i in range(len(lista)):
        if i > j:
            j = i
    return j

lista = [2,94,8,2,15,244,18,2,9489]

valor_maior= maior(lista)
print(valor_maior)
print(lista[valor_maior])