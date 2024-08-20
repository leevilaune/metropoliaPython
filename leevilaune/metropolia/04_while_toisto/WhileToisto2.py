while(True):
    tuuma = float(input("Anna tuumat: "))
    if(tuuma<0):
        print("Annoit negatiivisen tuumamäärän")
        break
    print("Senttimetrit:",tuuma*2.54)