lista = []

while(True):
    syote = input("Anna luku: ")
    if(syote==""):
        break;
    lista.append(int(syote))

lista.sort(reverse=True)
for i in range(5):
    print(lista[i])