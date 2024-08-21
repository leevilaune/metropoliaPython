airports = {}

while(True):
    user_input = input("Haluatko lisätä vai hakea?: ")
    if(user_input=="lopeta"):
        break
    if(user_input=="lisää"):
        icao = input("Anna ICAO: ")
        name = input("Anna nimi: ")
        airports[icao] = name
    elif(user_input=="hae"):
        icao = input("Anna ICAO: ")
        print(airports[icao])
