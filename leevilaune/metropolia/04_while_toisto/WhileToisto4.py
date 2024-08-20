from random import randint

numero = randint(1,10)
print(numero)
while(True):
    arvaus = int(input("Arvaa numero: "))
    if(arvaus==numero):
        print("Oikein")
        break
    elif(arvaus>numero):
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
