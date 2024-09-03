from distutils.command.install_egg_info import install_egg_info

import geopy
import mysql.connector
from geopy.distance import geodesic


def get_airport(icao):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
    return cursor.fetchall()

def calculate_distance(airport1, airport2):
    return geodesic((airport1[4],airport1[5]),(airport2[4],airport2[5]))

connection = mysql.connector.connect(host="127.0.0.1",
                                     port=3306,
                                     database="flight_game",
                                     username="root",
                                     password="secretpassword",
                                     autocommit=True)

icao1 = input("Anna ensimmäinen ICAO: ")
icao2 = input("Anna toinen ICAO: ")

print(calculate_distance(get_airport(icao1)[0],get_airport(icao2)[0]))
