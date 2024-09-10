import mysql.connector

def get_airports(iso_country):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM airport WHERE iso_country='{iso_country}'")
    return cursor.fetchall()

def count_airport_types(airports):
    airport_types = dict()
    for airport in airports:
        if airport_types.get(airport[2]) is not None:
            airport_types[airport[2]]+=1
        else:
            airport_types[airport[2]]=1
    return airport_types


connection = mysql.connector.connect(host="127.0.0.1",
                                     port=3306,
                                     database="flight_game",
                                     username="root",
                                     password="secretpassword",
                                     autocommit=True)

while(True):
    iso_country = input("Anna maatunnus: ")
    if iso_country== "":
        break
    types = count_airport_types(get_airports(iso_country))
    for type in types:
        print(f"{type}: {types[type]}")