"""
Aplicabilitate reala:
- Robotul urmareste muchii (margini) pentru a intelege obstacole si trasee.
Ce invatam:
- Blur pentru reducerea zgomotului.
- Detectie de muchii cu Canny.
De ce:
- Canny scoate in evidenta formele importante din scena.
"""

import os

import cv2 as cv


INPUT_PATH = "Course 4/assets/images/sudoku.png"
OUTPUT_DIR = "Course 4/assets/output"
if not os.path.exists(INPUT_PATH):
    INPUT_PATH = "assets/images/sudoku.png"
if not os.path.exists("Course 4/assets"):
    OUTPUT_DIR = "assets/output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    imagine = cv.imread(INPUT_PATH, cv.IMREAD_GRAYSCALE)
    if imagine is None:
        raise FileNotFoundError(f"Nu am gasit imaginea: {INPUT_PATH}")

    blur = cv.GaussianBlur(imagine, (5, 5), 0)
    muchii = cv.Canny(blur, 70, 180)

    out_path = OUTPUT_DIR + "/02_canny_edges.png"
    cv.imwrite(out_path, muchii)

    pixeli_muchie = int((muchii > 0).sum())
    print(f"[OK] Canny salvat: {out_path}")
    print(f"[INFO] Pixeli de muchie detectati: {pixeli_muchie}")


if __name__ == "__main__":
    main()
