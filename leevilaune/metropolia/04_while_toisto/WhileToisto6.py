from numpy import random
pisteet = int(input("Pisteiden kokonaismäärä: "))

i = 0

pisteLista = []
pisteetYmpyrässä = []

while(i<pisteet):
    piste = (random.uniform(-1.0,1.0),random.uniform(-1.0,1.0))
    pisteLista.append(piste)
    x = piste[0]
    y = piste[1]
    print(piste)
    if(x**2+y**2<=1):
        pisteetYmpyrässä.append(piste)
    i+=1

n = len(pisteetYmpyrässä)
N = len(pisteLista)
print("Pii:",4*n/N)