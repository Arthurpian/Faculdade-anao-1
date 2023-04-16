resposta = input("Voce quer conhecer minha calculadora ? (s/n)")
while resposta != "s" and resposta != "n":
    resposta = input("tem que ser (s/n)")
if resposta == "s":
    while True:
        num1 = input("Diga um numero : ")
        while not num1.isnumeric():
            num1 = input("Diga um numero : ")
        num1 = int(num1)
        num2 = input("Diga um numero : ")
        while not num2.isnumeric():
            num2 = input("Diga um numero : ")
        num2 = int(num2)
        opcao = input("O que voce deseja fazer ? (soma, subtração, divisão, multiplicação, ou sair ")
        while not (opcao == "soma" or opcao == "subtração" or opcao == "divisão" or
            opcao == "multiplicação" or opcao == "sair"):
            opcao = input("Mano vc é do java ? ta me tirano (soma, subtração, divisão, multiplicação, ou sair")
        if opcao == "soma":
            resultado = num1+num2
            print(f"A {opcao} entre {num1} e {num2} dá {resultado}")
        elif opcao == "multiplicação":
            resultado = num1*num2
            print(f"A {opcao} entre {num1} e {num2} dá {resultado}")
        elif opcao == "divisão":
            resultado = num1/num2
            print(f"A {opcao} entre {num1} e {num2} dá {resultado}")
        elif opcao == "subtração":
            resultado = num1-num2
            print(f"A {opcao} entre {num1} e {num2} dá {resultado}")
        else:
            print("Tchau")
            break
else:
    print("seu boboca vai cata coquinho")