from random import randint

def heita_noppaa(tahkot):
    return randint(1,tahkot)

tahkot = int(input("Anna tahkojen määrä: "))

while(True):
    noppa = heita_noppaa(tahkot)
    print(noppa)
    if(noppa == tahkot):
        break