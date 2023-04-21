qtd = 100
a = 1
b = 1
j = 0

while j < 100:
    c=a+b
    a=b
    i=2
    while i<c:
        if c%i==0:
            print(f"{j} teste: {c} não é primo pois {c}%{i}=0")
            break
        elif i >=c**(1/2):
            print(f"{j} teste : {c} é primo")
            qtd+=1
            break
        i+=1
    j+=1