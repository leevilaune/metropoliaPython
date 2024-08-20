import numpy

def pizzan_cm2_hinta(halkaisija, hinta):
    ala = 3.14*(halkaisija/2)**2
    return ala/hinta

pizza1_halkaisija = float(input("Anna ensimmäinen halkaisija: "))
pizza1_hinta = float(input("Anna ensimmäinen hinta: "))
pizza2_halkaisija = float(input("Anna toinen halkaisija: "))
pizza2_hinta = float(input("Anna toinen hinta: "))

pizza1_yksikkö_hinta = pizzan_cm2_hinta(pizza1_halkaisija,pizza1_hinta)
pizza2_yksikkö_hinta = pizzan_cm2_hinta(pizza2_halkaisija, pizza2_hinta)
if(pizza2_yksikkö_hinta>pizza1_yksikkö_hinta):
    print("Pizza 1 antaa paremman vastineen rahalle")
elif(pizza1_yksikkö_hinta>pizza2_yksikkö_hinta):
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Vastine on sama molemmille pizzoille")