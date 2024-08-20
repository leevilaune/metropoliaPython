tunnus = "python"
salasana = "rules"

vaarat_arvaukset = 0

while(True):
    if(vaarat_arvaukset>=5):
        break
    annettu_tunnus = input("Anna käyttäjätunnut: ")
    annettu_salasana = input("Anna salasana: ")
    if(annettu_tunnus==tunnus and annettu_salasana==salasana):
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        vaarat_arvaukset+=1
