"""
Aplicabilitate reala:
- Robotul combina date din senzori diferiti (distanta + temperatura) pentru context.
Ce invatam:
- Procesare paralela a mai multor fluxuri de telemetrie.
De ce:
- In productie, deciziile bune apar din fuziunea simultana a mai multor masuratori.
"""

import threading
import time


distante = [10, 15, 8, 20]
temperaturi = [30, 32, 35, 31]


def analizeaza_distante():
    # Parcurgem datele radarului.
    for distanta in distante:
        print(f"[Radar] Distanta detectata: {distanta} cm")
        time.sleep(1)


def analizeaza_temperaturi():
    # Parcurgem datele termometrului.
    for temperatura in temperaturi:
        print(f"[Termometru] Temperatura detectata: {temperatura} C")
        time.sleep(1)


if __name__ == "__main__":
    fir_radar = threading.Thread(target=analizeaza_distante)
    fir_termometru = threading.Thread(target=analizeaza_temperaturi)

    fir_radar.start()
    fir_termometru.start()

    fir_radar.join()
    fir_termometru.join()
    print("Analiza listelor s-a terminat.")
