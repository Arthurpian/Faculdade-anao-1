print("Bem vindo\nFaça agora seu cadastro")
login = input("Crie seu login: ")
senha = input("Crie sua senha: ")

while login == senha:
    print("Login é senha não pode ser iguais \nRefaça seu cadastro")
    login = input("Crie seu login: ")
    senha = input("Crie sua senha: ")

print("Conta criada")