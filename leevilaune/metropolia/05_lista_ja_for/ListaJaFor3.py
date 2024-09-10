while(True):
    luku = int(input("Anna luku: "))

    on_alkuluku = True

    for i in range(luku // 2):
        i += 2
        print(i)
        if (luku % i == 0):
            on_alkuluku = False
            print("Ei ole alkuluku")
            break
    if (on_alkuluku):
        print("on alkuluku")