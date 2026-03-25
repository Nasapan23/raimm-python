"""
Aplicabilitate reala:
- Controllerul robotului pastreaza starea actuatorilor intr-un registru comun.
Ce invatam:
- Actualizari concurente pe acelasi dictionar, sincronizate cu lock.
De ce:
- Operatorul trebuie sa vada un status coerent al rotilor, nu valori amestecate.
"""

import threading
import time


status_robot = {"roata_stanga": "Oprita", "roata_dreapta": "Oprita"}
lacat_status = threading.Lock()


def porneste_roata_stanga():
    time.sleep(2)
    with lacat_status:
        status_robot["roata_stanga"] = "Merge"
        print(f"[Update] {status_robot}")


def porneste_roata_dreapta():
    time.sleep(3)
    with lacat_status:
        status_robot["roata_dreapta"] = "Merge"
        print(f"[Update] {status_robot}")


if __name__ == "__main__":
    fir_stanga = threading.Thread(target=porneste_roata_stanga)
    fir_dreapta = threading.Thread(target=porneste_roata_dreapta)

    fir_stanga.start()
    fir_dreapta.start()
    fir_stanga.join()
    fir_dreapta.join()

    print(f"Status final: {status_robot}")
