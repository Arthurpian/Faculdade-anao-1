lista = ["Allen", "Dan", "Well", "Piezo"]
frase = ""

for i in range(len(lista)):
    if i == len(lista)-1:
        frase += f" e o {lista[i]}"
        continue
    frase += f"o {lista[i]}"
    if i<len(lista)-2:
        frase+=", "
frase+= " são professores"

print(frase)
