"""
Aplicabilitate reala:
- Robotul identifica obiecte pe masa dupa contur.
Ce invatam:
- Threshold + findContours.
- Desenare contururi si bounding boxes.
De ce:
- Contururile ajuta la separarea obiectelor fata de fundal.
"""

import os

import cv2 as cv


INPUT_PATH = "Course 4/assets/images/smarties.png"
OUTPUT_DIR = "Course 4/assets/output"
if not os.path.exists(INPUT_PATH):
    INPUT_PATH = "assets/images/smarties.png"
if not os.path.exists("Course 4/assets"):
    OUTPUT_DIR = "assets/output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    imagine = cv.imread(INPUT_PATH)
    if imagine is None:
        raise FileNotFoundError(f"Nu am gasit imaginea: {INPUT_PATH}")

    gri = cv.cvtColor(imagine, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gri, (5, 5), 0)
    _, mask = cv.threshold(blur, 60, 255, cv.THRESH_BINARY_INV)

    contururi, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    desen = imagine.copy()
    obiecte = 0
    for contur in contururi:
        aria = cv.contourArea(contur)
        if aria < 80:
            continue
        obiecte += 1
        x, y, w, h = cv.boundingRect(contur)
        cv.rectangle(desen, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.drawContours(desen, [contur], -1, (255, 0, 0), 2)

    out_path = OUTPUT_DIR + "/03_contours_boxes.png"
    cv.imwrite(out_path, desen)

    print(f"[OK] Contours salvat: {out_path}")
    print(f"[INFO] Obiecte detectate: {obiecte}")


if __name__ == "__main__":
    main()
