sukupuoli = input("Anna biologinen sukupuoli: ")
hemoglob = int(input("Anna hemoglobiini: "))

if(sukupuoli=="Nainen"):
    if(hemoglob<117):
        print("Hemoglobiini on alhainen")
    elif(hemoglob>175):
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
elif(sukupuoli=="Mies"):
    if(hemoglob<134):
        print("Hemoglobiini on alhainen")
    elif(hemoglob>195):
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
else:
    print("Jokin meni vikaan, todennäköisesti kirjoitit sukupuolen väärin")
    print("Vaihtoehdot ovat Mies ja Nainen")