def verificar(msg, opcoes):
    opcao = input(msg)
    while opcao not in opcoes:
        print("Digite uma palavra valida")
        opcao = input(msg)
    return opcao

vinhos = ["rose", "branco", "tinto"]
tipo_de_vinho = verificar("Qual vinho voce quer: rose , branco , tinto ?", vinhos)
print(tipo_de_vinho)

