"""
Aplicabilitate reala:
- Un brat robotic aduna si consuma piese dintr-un buffer comun.
Ce invatam:
- Pattern producer-consumer simplificat, protejat cu lock.
De ce:
- Fara control concurent, pot aparea erori la accesul simultan in inventar.
"""

import threading
import time


class BratRobotic:
    def __init__(self):
        self.inventar = []
        self.lacat = threading.Lock()

    def aduna_piese(self):
        for _ in range(5):
            time.sleep(0.5)
            with self.lacat:
                self.inventar.append("Piesa")
                print(f"[Aduna] Inventar curent: {len(self.inventar)} piese")

    def consuma_piese(self):
        for _ in range(5):
            time.sleep(0.5)
            with self.lacat:
                if len(self.inventar) > 0:
                    self.inventar.pop()
                    print(f"[Consuma] Inventar curent: {len(self.inventar)} piese")
                else:
                    print("[Consuma] Nu exista piese de consumat.")


if __name__ == "__main__":
    brat = BratRobotic()

    fir_adunare = threading.Thread(target=brat.aduna_piese)
    fir_consum = threading.Thread(target=brat.consuma_piese)

    fir_adunare.start()
    fir_consum.start()
    fir_adunare.join()
    fir_consum.join()

    print(f"Inventar final: {brat.inventar}")
