i = 2
num = 3

while i < num:
    print(f"{num}%{i}={num%i}")
    if num%i==0:
        print("Não é primo")
        break
    elif i>=num/2:
        print("É primo")
        break
    i+=1