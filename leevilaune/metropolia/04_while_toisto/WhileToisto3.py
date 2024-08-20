numerot = []

while(True):
    numero = input("Anna numero: ")
    if(numero==""):
        break;
    numerot.append(int(numero))

print("Pienin",min(numerot))
print("Suurin", max(numerot))