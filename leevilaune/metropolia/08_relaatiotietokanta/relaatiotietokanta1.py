import mysql.connector

def get_airport(icao):
    cursor = connection.cursor()
    if icao.find("'") or icao.find('"'):
        print("Trying to SQL Inject?")
        return
    cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
    return cursor.fetchall()

connection = mysql.connector.connect(host="127.0.0.1",
                                     port=3306,
                                     database="flight_game",
                                     username="root",
                                     password="secretpassword",
                                     autocommit=True)

while(True):
    icao = input("Anna ICAO-tunnus: ")
    if(icao==""):
        break
    airport = get_airport(icao)[0]
    print(f"Nimi:  {airport[3]}")
    print(f"Kunta: {airport[10]}")