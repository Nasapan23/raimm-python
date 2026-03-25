"""
Aplicabilitate reala:
- O drona are comenzi concurente (urcare/coborare) din subsisteme diferite.
Ce invatam:
- Mostenire OOP pentru reutilizarea bazei si Lock pentru protejarea altitudinii.
De ce:
- Altitudinea este resursa critica; valorile gresite pot produce erori de navigatie.
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
                print(f"[{self.nume}] Urca -> {self.altitudine} m")

    def coboara(self):
        for _ in range(5):
            time.sleep(0.5)
            with self.lacat:
                self.altitudine -= 5
                print(f"[{self.nume}] Coboara -> {self.altitudine} m")


if __name__ == "__main__":
    drona = DronaLivrare("Drona-RAIMM")

    fir_urcare = threading.Thread(target=drona.urca)
    fir_coborare = threading.Thread(target=drona.coboara)

    fir_urcare.start()
    fir_coborare.start()
    fir_urcare.join()
    fir_coborare.join()

    print(f"Altitudine finala: {drona.altitudine} m (asteptat: 25 m)")
