"""
Aplicabilitate reala:
- Robotii lucreaza cu telemetrie grupata in structuri de date centralizate.
Ce invatam:
- Dictionar pentru stocarea rapida a valorilor de la senzori.
De ce:
- E usor de extins (adaugam senzori noi) si de citit de catre alte module.
"""

import threading


# Nivelul 1: dictionar simplu cu datele de la senzori.
senzori_robot = {"temperatura": 45, "umiditate": 80}


def afiseaza_senzori():
    # Functie simpla rulata pe thread, ca introducere in exercitiu.
    print(f"Temperatura: {senzori_robot['temperatura']} C")
    print(f"Umiditate: {senzori_robot['umiditate']} %")


if __name__ == "__main__":
    fir_senzori = threading.Thread(target=afiseaza_senzori)
    fir_senzori.start()
    fir_senzori.join()
    print("Citirea senzorilor a fost finalizata.")
