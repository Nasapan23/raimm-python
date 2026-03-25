"""
Aplicabilitate reala:
- In robotica, mai multe subsisteme pot modifica nivelul bateriei in acelasi timp.
Ce invatam:
- OOP pentru modelarea robotului + Lock pentru sincronizarea accesului la baterie.
De ce:
- Fara lock apar valori incorecte, iar deciziile de control devin nesigure.
"""

import threading
import time


class RobotAutonom:
    def __init__(self):
        self.nivel_baterie = 50
        self.lacat_baterie = threading.Lock()

    def consuma_baterie(self):
        for _ in range(3):
            time.sleep(0.5)
            # Blocam accesul la baterie cat timp o modificam.
            with self.lacat_baterie:
                self.nivel_baterie -= 10
                print(f"[-] Motorul consuma. Baterie: {self.nivel_baterie}%")

    def incarca_solar(self):
        for _ in range(3):
            time.sleep(0.5)
            # Acelasi lacat protejeaza aceeasi resursa comuna.
            with self.lacat_baterie:
                self.nivel_baterie += 10
                print(f"[+] Soarele incarca. Baterie: {self.nivel_baterie}%")


if __name__ == "__main__":
    wall_e = RobotAutonom()

    t1 = threading.Thread(target=wall_e.consuma_baterie)
    t2 = threading.Thread(target=wall_e.incarca_solar)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Baterie finala (corecta datorita Lock-ului): {wall_e.nivel_baterie}%")
