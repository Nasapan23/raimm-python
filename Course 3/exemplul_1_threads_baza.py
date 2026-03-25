"""
Aplicabilitate reala:
- Un robot mobil trebuie sa se deplaseze si sa citeasca senzori simultan.
Ce invatam:
- Thread-uri separate pentru task-uri independente (locomotie + perceptie).
De ce:
- Evitam blocarea robotului cat timp asteapta finalizarea unei singure actiuni.
"""

import threading
import time


def misca_robotul():
    # Simulam deplasarea robotului.
    print("[Motor] Robotul a pornit la drum...")
    time.sleep(3)
    print("[Motor] Robotul a ajuns!")


def citeste_senzor():
    # Simulam citirea senzorului de distanta din secunda in secunda.
    for secunda in range(4):
        print(f"[Senzor] Distanta e OK la secunda {secunda}")
        time.sleep(1)


if __name__ == "__main__":
    thread_motor = threading.Thread(target=misca_robotul)
    thread_senzor = threading.Thread(target=citeste_senzor)

    print("--- START MISIUNE ---")
    thread_motor.start()
    thread_senzor.start()

    # Programul principal asteapta finalizarea ambelor task-uri.
    thread_motor.join()
    thread_senzor.join()
    print("--- MISIUNE COMPLETA ---")
