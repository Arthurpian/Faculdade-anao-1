valor = 1000
mensal = 200
meses = 24
i = 0
rendimento = valor * 1.01

while i <= 23:

    print(f"Valor atual {valor:.2f} dia final {rendimento:.2f}")
    valor = rendimento
    valor += 200
    rendimento = valor * 1.01

    i+=1