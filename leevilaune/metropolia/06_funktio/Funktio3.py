

def gallonat_litroiksi(gallonat):
    return gallonat*3.785

while(True):
    gallonat = float(input("Anna gallonat: "))
    if(gallonat < 0):
        break
    print(f"{gallonat} gallonaa on litroina {gallonat_litroiksi(gallonat)}")