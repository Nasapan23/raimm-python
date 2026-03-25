"""
Aplicabilitate reala:
- Este aceeasi situatie din problema 4, dar reparata prin sincronizare corecta.
Ce invatam:
- Lock-ul transforma accesul concurent intr-un acces controlat, sigur.
De ce:
- Datele de baterie devin deterministe, deci logica de control poate fi de incredere.
"""

import threading


baterie = 1_000_000
lacat = threading.Lock()


def consuma():
    global baterie

    for _ in range(500_000):
        # Lock-ul face operatia de decrement sigura.
        with lacat:
            baterie -= 1


def incarca():
    global baterie

    for _ in range(500_000):
        # Lock-ul face operatia de increment sigura.
        with lacat:
            baterie += 1


if __name__ == "__main__":
    fir_consuma = threading.Thread(target=consuma)
    fir_incarca = threading.Thread(target=incarca)

    fir_consuma.start()
    fir_incarca.start()
    fir_consuma.join()
    fir_incarca.join()

    print(f"Baterie finala (cu lock): {baterie}")
    print("Rezultatul trebuie sa fie exact 1000000.")
