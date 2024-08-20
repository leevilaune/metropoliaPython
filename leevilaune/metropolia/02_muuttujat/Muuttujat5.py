import math
from math import floor

leviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#muutetaan kaikki luodeiksi
nauloiksi = leviskat*20+naulat
luodeiksi = nauloiksi*32+luodit

#lasketaan paino ja muutetaan kiloiksi ja grammoiksi
paino = float(luodeiksi * 13.3)
kilot = floor(paino/1000)
grammat = paino/1000-(floor(paino/1000))
grammat = round(grammat*1000,5)
print(kilot,"kilogrammaa ja ",grammat, "grammaa.")