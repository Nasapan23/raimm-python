"""
Aplicabilitate reala:
- Simulam o problema clasica: doua procese modifica acelasi nivel de energie.
Ce invatam:
- Fara sincronizare apare race condition si rezultatul final devine imprevizibil.
De ce:
- In sisteme embedded, astfel de erori duc la telemetrie falsa si decizii gresite.
"""

import threading
import time


baterie = 1_000_000


def consuma():
    global baterie

    # Scadem bateria fara lock (intentionat gresit).
    for i in range(500_000):
        baterie -= 1
        if i % 1000 == 0:
            # Fortam alternarea firelor ca sa observam mai usor race condition.
            time.sleep(0)


def incarca():
    global baterie

    # Incarcam bateria fara lock (intentionat gresit).
    for i in range(500_000):
        baterie += 1
        if i % 1000 == 0:
            time.sleep(0)


if __name__ == "__main__":
    fir_consuma = threading.Thread(target=consuma)
    fir_incarca = threading.Thread(target=incarca)

    fir_consuma.start()
    fir_incarca.start()
    fir_consuma.join()
    fir_incarca.join()

    print(f"Baterie finala (fara lock): {baterie}")
    print("Valoarea corecta ar fi 1000000, dar race condition poate strica rezultatul.")
