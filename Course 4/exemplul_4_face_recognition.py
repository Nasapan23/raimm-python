"""
Aplicabilitate reala:
- Robotul de receptie recunoaste persoanele cunoscute.
Ce invatam:
- Detectie fata cu Haar Cascade.
- "Enrolare" persoane cunoscute si comparare pe histograma fetei.
De ce:
- Este un prim pas simplu spre sisteme reale de face recognition.
"""

import os

import cv2 as cv
import numpy as np


FACES_DIR = "Course 4/assets/faces"
CASCADE_PATH = "Course 4/assets/models/haarcascade_frontalface_default.xml"
OUTPUT_DIR = "Course 4/assets/output"
if not os.path.exists(FACES_DIR):
    FACES_DIR = "assets/faces"
if not os.path.exists(CASCADE_PATH):
    CASCADE_PATH = "assets/models/haarcascade_frontalface_default.xml"
if not os.path.exists("Course 4/assets"):
    OUTPUT_DIR = "assets/output"


def extrage_fete(imagine_bgr, detector):
    gri = cv.cvtColor(imagine_bgr, cv.COLOR_BGR2GRAY)
    fete = detector.detectMultiScale(gri, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    return sorted(fete, key=lambda f: f[2] * f[3], reverse=True)


def histograma_fata(imagine_bgr, zona_fata):
    x, y, w, h = zona_fata
    gri = cv.cvtColor(imagine_bgr, cv.COLOR_BGR2GRAY)
    roi = gri[y : y + h, x : x + w]
    roi = cv.resize(roi, (120, 120))
    hist = cv.calcHist([roi], [0], None, [64], [0, 256])
    return cv.normalize(hist, hist).flatten()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    detector = cv.CascadeClassifier(CASCADE_PATH)
    if detector.empty():
        raise RuntimeError(f"Nu pot incarca detectorul: {CASCADE_PATH}")

    known = {
        "Barack Obama": FACES_DIR + "/obama.jpg",
        "Joe Biden": FACES_DIR + "/biden.jpg",
    }

    baza_date = {}
    for nume, path_imagine in known.items():
        imagine = cv.imread(path_imagine)
        if imagine is None:
            raise FileNotFoundError(f"Nu am gasit imaginea: {path_imagine}")

        fete = extrage_fete(imagine, detector)
        if not fete:
            raise RuntimeError(f"Nu am detectat fata pentru: {nume}")
        baza_date[nume] = histograma_fata(imagine, fete[0])

    test_path = FACES_DIR + "/obama2.jpg"
    test = cv.imread(test_path)
    if test is None:
        raise FileNotFoundError(f"Nu am gasit imaginea de test: {test_path}")

    fete_test = extrage_fete(test, detector)
    if not fete_test:
        raise RuntimeError("Nu am detectat nicio fata in imaginea de test.")

    for x, y, w, h in fete_test:
        hist_test = histograma_fata(test, (x, y, w, h))
        scoruri = {}
        for nume, hist in baza_date.items():
            scor = cv.compareHist(hist_test.astype(np.float32), hist.astype(np.float32), cv.HISTCMP_BHATTACHARYYA)
            scoruri[nume] = scor

        nume_castigator = min(scoruri, key=scoruri.get)
        distanta = scoruri[nume_castigator]
        eticheta = nume_castigator if distanta < 0.5 else "Necunoscut"

        cv.rectangle(test, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(
            test,
            f"{eticheta} ({distanta:.2f})",
            (x, y - 10),
            cv.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )
        print(f"[INFO] Predictie: {eticheta} | distanta: {distanta:.3f}")

    out_path = OUTPUT_DIR + "/04_face_recognition_result.png"
    cv.imwrite(out_path, test)
    print(f"[OK] Rezultat salvat: {out_path}")


if __name__ == "__main__":
    main()
