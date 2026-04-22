"""
Aplicabilitate reala:
- Camera robotului transforma imaginea color in alb-negru pentru detectie mai rapida.
Ce invatam:
- Conversia BGR -> grayscale.
- Threshold simplu pentru imagine binara (BW).
De ce:
- Multi algoritmi de viziune functioneaza mai stabil pe imagini simplificate.
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

    imagine = cv.imread(INPUT_PATH)
    if imagine is None:
        raise FileNotFoundError(f"Nu am gasit imaginea: {INPUT_PATH}")

    gri = cv.cvtColor(imagine, cv.COLOR_BGR2GRAY)
    _, bw = cv.threshold(gri, 120, 255, cv.THRESH_BINARY)

    out_gray = OUTPUT_DIR + "/01_grayscale.png"
    out_bw = OUTPUT_DIR + "/01_bw_threshold.png"
    cv.imwrite(out_gray, gri)
    cv.imwrite(out_bw, bw)

    print(f"[OK] Grayscale salvat: {out_gray}")
    print(f"[OK] BW salvat: {out_bw}")


if __name__ == "__main__":
    main()
