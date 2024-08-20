from random import randint

def heita_noppaa():
    return randint(1,6)

while(True):
    noppa = heita_noppaa()
    print(noppa)
    if(noppa == 6):
        break