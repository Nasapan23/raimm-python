"""
Aplicabilitate reala:
- Mini-arhitectura de sistem robotic: consum energetic, incarcare urgenta, comenzi operator.
Ce invatam:
- Orchestrare thread-uri + lock + bucla de comenzi intr-o clasa centrala de control.
De ce:
- Aproape orice robot real are nevoie de management energetic si oprire controlata.
"""

import threading
import time


class RobotOS:
    def __init__(self):
        self.baterie = 100
        self.lacat_baterie = threading.Lock()
        self.activ = True

    def consum_fundal(self):
        # Cat timp robotul e activ, bateria scade in fundal.
        while self.activ:
            time.sleep(2)
            with self.lacat_baterie:
                self.baterie = max(0, self.baterie - 5)
                print(f"[Consum] Baterie: {self.baterie}%")

                if self.baterie == 0:
                    print("[Consum] Bateria a ajuns la 0%. Robotul se opreste.")
                    self.activ = False

    def incarcare_urgenta(self):
        # Dupa 7 secunde incepem monitorizarea pentru incarcare de urgenta.
        # Cerinta ramane aceeasi: se aplica o singura data cand bateria scade sub 70%.
        time.sleep(7)

        while self.activ:
            with self.lacat_baterie:
                if self.baterie < 70:
                    self.baterie = min(100, self.baterie + 40)
                    print(f"[Urgenta] Incarcare aplicata. Baterie: {self.baterie}%")
                    return

            # Verificam periodic pana cand pragul este atins sau robotul se opreste.
            time.sleep(1)

        print("[Urgenta] Robotul s-a oprit inainte de incarcare.")


if __name__ == "__main__":
    robot = RobotOS()

    fir_consum = threading.Thread(target=robot.consum_fundal)
    fir_incarcare = threading.Thread(target=robot.incarcare_urgenta)

    fir_consum.start()
    fir_incarcare.start()

    # Firul principal asculta comenzi cat timp robotul ruleaza.
    while robot.activ:
        try:
            comanda = input("Comanda: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            comanda = "oprire"

        if comanda == "oprire":
            robot.activ = False
        else:
            print("Comanda necunoscuta. Scrie 'oprire' ca sa inchizi programul.")

    fir_consum.join()
    fir_incarcare.join()
    print("RobotOS s-a inchis elegant.")
