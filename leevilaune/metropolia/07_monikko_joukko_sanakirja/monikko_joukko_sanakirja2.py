names = set()

def print_names(names):
    for i in names:
        print(i)

while(True):
    name = input("Anna nimi: ")
    if(name==""):
        break
    names.add(name)

print_names(names)