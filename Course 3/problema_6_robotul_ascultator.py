"""
Aplicabilitate reala:
- Un robot de patrulare ruleaza continuu, dar primeste comenzi de la operator.
Ce invatam:
- Bucla de fundal controlata printr-o variabila de stare partajata.
De ce:
- Oprirea controlata este esentiala pentru siguranta in teren.
"""

import threading
import time


patruleaza = True


def miscare():
    global patruleaza

    # Robotul patruleaza pana cand variabila globala devine False.
    while patruleaza:
        print("Robotul patruleaza...")
        time.sleep(2)

    print("Patrularea s-a oprit.")


if __name__ == "__main__":
    fir_miscare = threading.Thread(target=miscare)
    fir_miscare.start()

    while True:
        comanda = input("Scrie STOP pentru a opri: ").strip()
        if comanda == "STOP":
            patruleaza = False
            break

        print("Comanda invalida. Trebuie exact STOP.")

    fir_miscare.join()
    print("Robotul s-a oprit corect.")
