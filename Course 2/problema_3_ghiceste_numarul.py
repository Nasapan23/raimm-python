numar_secret = 42
# numar_secret = random.randint(1, 100) # Pentru a genera un numar secret aleator intre 1 si 100

while True:
    ghicire = int(input("Ghiceste numarul secret: "))

    if ghicire < numar_secret:
        print("Prea mic!")
    elif ghicire > numar_secret:
        print("Prea mare!")
    else:
        print("Bravo, ai ghicit!")
        break
