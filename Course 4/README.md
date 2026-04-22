# Crash Course Python (103) - RAIMM

Acest folder contine exemple scurte pentru **Course 4 (Computer Vision cu OpenCV)**:
- transformare BW (alb-negru)
- detectie muchii cu Canny
- detectie contururi
- face recognition basic (detectie + identificare simpla)
- bonus: detectie obiecte YOLO pe camera live cu UI Tkinter

## Structura
- `exemplul_1_bw_transform.py` - grayscale + threshold BW
- `exemplul_2_canny.py` - detectie muchii
- `exemplul_3_contours.py` - contururi + bounding boxes
- `exemplul_4_face_recognition.py` - detectie fata + clasificare simpla
- `bonus_exercise_yolo_live_tkinter.py` - YOLO live + UI Tkinter + lista obiecte detectate
- `programa_course_4.md` - programa scurta de predat
- `assets/` - imagini + model Haar + rezultate generate

## Rulare
Din radacina proiectului:

```bash
python -m pip install -r "Course 4/requirements.txt"
python "Course 4/exemplul_1_bw_transform.py"
python "Course 4/exemplul_2_canny.py"
python "Course 4/exemplul_3_contours.py"
python "Course 4/exemplul_4_face_recognition.py"
python "Course 4/bonus_exercise_yolo_live_tkinter.py"
```

Rezultatele se salveaza in `Course 4/assets/output`.
Pentru bonusul live cu YOLO:
- apasa `Start` (autodetecteaza camera),
- apasa `Stop` la final (sau inchide fereastra).
- la prima rulare poate dura mai mult (se descarca modelul `yolov8n.pt`).

## Rulare recomandata (venv local)
Din `Course 4`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe bonus_exercise_yolo_live_tkinter.py
```

Pe Windows, evita `py bonus_exercise_yolo_live_tkinter.py` cand lucrezi dintr-un venv activat.
Pentru acest curs, foloseste `python ...` sau direct `.\.venv\Scripts\python.exe ...`, altfel poti porni alt interpreter fara pachetele instalate.
