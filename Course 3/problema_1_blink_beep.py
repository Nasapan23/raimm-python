"""
Aplicabilitate reala:
- Robotul comunica starea prin canale multiple: vizual (LED) si audio (beep).
Ce invatam:
- Doua thread-uri pentru doua semnale care trebuie sa ruleze simultan.
De ce:
- Interfata de stare devine mai clara pentru operator in timp real.
"""

import threading
import time


def clipeste_led():
    # LED-ul clipeste de 5 ori, la interval de 1 secunda.
    for _ in range(5):
        print("[LED] Blink!")
        time.sleep(1)


def scoate_sunet():
    # Difuzorul scoate bip de 5 ori, la interval de 1.5 secunde.
    for _ in range(5):
        print("[Difuzor] Beep!")
        time.sleep(1.5)


if __name__ == "__main__":
    fir_led = threading.Thread(target=clipeste_led)
    fir_sunet = threading.Thread(target=scoate_sunet)

    fir_led.start()
    fir_sunet.start()

    fir_led.join()
    fir_sunet.join()
    print("Blink & Beep finalizat.")
