vuosi = int(input("Anna vuosi: "))

if(vuosi%4==0):
    if(vuosi%100==0):
        if(vuosi%400==0):
            print("On karkausvuosi")
        else:
            print("Ei ole karkausvuosi")
    else:
        print("karkausvuosi")
else:
    print("Ei ole karkausvuosi")