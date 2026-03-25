"""
Aplicabilitate reala:
- Un sistem de monitorizare termica trebuie sa detecteze rapid supraincalzirea.
Ce invatam:
- Un thread monitorizeaza continuu, alt thread simuleaza interventia de racire.
De ce:
- In sisteme reale, detectia si actiunea corectiva ruleaza in paralel.
"""

import threading
import time


senzori_robot = {"temperatura": 45, "umiditate": 80}
lacat_senzori = threading.Lock()


def alarma():
    # Verifica periodic temperatura; se opreste singura cand devine sigura.
    while True:
        with lacat_senzori:
            temperatura_curenta = senzori_robot["temperatura"]

        if temperatura_curenta > 40:
            print("PERICOL SUPRAINCALZIRE!")
        else:
            print("Temperatura a revenit in limite normale.")
            break

        time.sleep(2)


def scade_temp():
    # Dupa 5 secunde, sistemul de racire coboara temperatura.
    time.sleep(5)
    with lacat_senzori:
        senzori_robot["temperatura"] = 30
    print("Sistemul de racire a setat temperatura la 30C.")


if __name__ == "__main__":
    fir_alarma = threading.Thread(target=alarma)
    fir_racire = threading.Thread(target=scade_temp)

    fir_alarma.start()
    fir_racire.start()

    fir_alarma.join()
    fir_racire.join()
    print("Monitorizarea temperaturii s-a incheiat.")
