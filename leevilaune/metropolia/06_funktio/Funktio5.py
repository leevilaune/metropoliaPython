def poista_parittomat(lista):
    parilliset = []
    for i in lista:
        if(i%2==0):
            parilliset.append(i)
    return parilliset

lukuja = [3,4,5,2,3,7,1,4,8]
print(f"Alkuperäinen: {lukuja}")
print(f"Parsittu: {poista_parittomat(lukuja)}")