"""
Aplicabilitate reala:
- Robotul ruleaza autonom (scanare), dar operatorul trebuie sa il poata opri instant.
Ce invatam:
- Background thread pentru sarcina repetitiva + fir principal pentru comenzi umane.
De ce:
- Separarea clarifica arhitectura HMI (human-machine interface) in robotica.
"""

import threading
import time


robot_activ = True


def scanare_fundal():
    global robot_activ

    # Thread de fundal: ruleaza continuu pana cand robot_activ devine False.
    while robot_activ:
        print("Robotul scaneaza zona...")
        time.sleep(1)

    print("Scanarea de fundal s-a oprit.")


if __name__ == "__main__":
    fir_scanare = threading.Thread(target=scanare_fundal)
    fir_scanare.start()

    while True:
        comanda = input("Comanda (scrie 'stop' pentru oprire): ").strip().lower()
        if comanda == "stop":
            robot_activ = False
            break

        print("Comanda necunoscuta. Incearca din nou.")

    fir_scanare.join()
    print("Program inchis elegant.")
