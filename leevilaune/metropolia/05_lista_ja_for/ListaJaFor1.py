from random import random, randint

noppia = int(input("Kuinka monta noppaa heitetään? "))

summa = 0
for i in range(noppia):
    noppa = randint(1,6)
    print(f"Noppa {i}:",noppa)
    summa += noppa
print("Silmälukujen summa: ",summa)