while True:
   nota = input("Qual foi a sua nota d 0 a 10: ")
   if nota.isnumeric():
      nota = int(nota)
      if nota >0 and nota <10:
         break
      else:
         continue
print(f"Sua nota é {nota}")