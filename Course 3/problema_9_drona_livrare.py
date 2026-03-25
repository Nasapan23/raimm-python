"""
Aplicabilitate reala:
- Drona de livrare combina comenzi verticale din module diferite de control.
Ce invatam:
- Mostenire pentru modelul de zbor si lock pentru stare comuna (altitudine).
De ce:
- Previne inconsistentele in telemetria de zbor in scenarii concurente.
"""

import threading
import time


class AparatZbor:
    def __init__(self, nume):
        self.nume = nume
        self.altitudine = 0
        self.lacat = threading.Lock()


class DronaLivrare(AparatZbor):
    def urca(self):
        for _ in range(5):
            time.sleep(0.5)
            with self.lacat:
                self.altitudine += 10
                print(f"[{self.nume}] Urca la {self.altitudine} m")

    def coboara(self):
        for _ in range(5):
            time.sleep(0.5)
            with self.lacat:
                self.altitudine -= 5
                print(f"[{self.nume}] Coboara la {self.altitudine} m")


if __name__ == "__main__":
    drona = DronaLivrare("Drona-Curier")

    fir_urca = threading.Thread(target=drona.urca)
    fir_coboara = threading.Thread(target=drona.coboara)

    fir_urca.start()
    fir_coboara.start()
    fir_urca.join()
    fir_coboara.join()

    print(f"Altitudine finala: {drona.altitudine} m (asteptat 25 m)")
