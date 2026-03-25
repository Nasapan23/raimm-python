"""
Aplicabilitate reala:
- Detectam depasirea unei limite critice de temperatura la motor.
Ce invatam:
- Un thread produce evenimentul (crestere temp), altul il detecteaza (alarma).
De ce:
- Este modelul de baza pentru sisteme de siguranta in timp real.
"""

import threading
import time


senzori = {"temp_motor": 35}
lacat = threading.Lock()


def monitorizare_alarma():
    # Thread-ul verifica periodic temperatura motorului.
    while True:
        with lacat:
            temp_curenta = senzori["temp_motor"]

        if temp_curenta > 50:
            print("ALARMA!")
            break

        print(f"Temperatura motor inca este sigura: {temp_curenta} C")
        time.sleep(0.5)


def creste_temperatura():
    # Simulam supraincalzirea dupa 3 secunde.
    time.sleep(3)
    with lacat:
        senzori["temp_motor"] = 60
    print("Temperatura motorului a crescut la 60C.")


if __name__ == "__main__":
    fir_alarma = threading.Thread(target=monitorizare_alarma)
    fir_supra = threading.Thread(target=creste_temperatura)

    fir_alarma.start()
    fir_supra.start()

    fir_alarma.join()
    fir_supra.join()
    print("Testul de alarma a fost finalizat.")
