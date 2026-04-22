"""
Aplicabilitate reala:
- Un robot poate "vedea" obiectele din jur in timp real si decide ce face.
Ce invatam:
- YOLO pentru detectie obiecte pe camera live.
- Tkinter pentru UI simplu (Start/Stop + afisare obiecte detectate).
De ce:
- Legam computer vision modern cu o interfata practica, usor de extins.
"""

from collections import Counter
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

BASE_DIR = Path(__file__).resolve().parent
REQUIREMENTS_PATH = BASE_DIR / "requirements.txt"
MODEL_PATH = BASE_DIR / "yolov8n.pt"


def raise_missing_dependency(package_name, exc):
    raise SystemExit(
        f"Lipseste pachetul `{package_name}`.\n"
        f"Instaleaza dependintele cu:\n"
        f'  python -m pip install -r "{REQUIREMENTS_PATH}"\n'
        "Daca folosesti un venv pe Windows, ruleaza scriptul cu `python`, nu cu `py`."
    ) from exc


try:
    import cv2 as cv
except ModuleNotFoundError as exc:
    raise_missing_dependency("opencv-python", exc)

try:
    from PIL import Image, ImageTk
except ModuleNotFoundError as exc:
    raise_missing_dependency("Pillow", exc)

try:
    from ultralytics import YOLO
except ModuleNotFoundError as exc:
    raise_missing_dependency("ultralytics", exc)

CONF_THRESHOLD = 0.45
UPDATE_MS = 30

# Variabile globale (intentionat simplu pentru cursanti non-tehnici).
model = None
capture = None
running = False
last_photo = None

root = None
status_var = None
video_canvas = None
detected_text = None
start_btn = None
stop_btn = None


def build_ui():
    global root, status_var, video_canvas, detected_text, start_btn, stop_btn

    root = tk.Tk()
    root.title("Bonus Exercise - YOLO Live Detection")
    root.geometry("1060x720")

    container = ttk.Frame(root, padding=12)
    container.pack(fill=tk.BOTH, expand=True)

    title = ttk.Label(
        container,
        text="YOLO Live Camera - Detectie Automata Obiecte",
        font=("Segoe UI", 16, "bold"),
    )
    title.pack(anchor="w", pady=(0, 10))

    controls = ttk.Frame(container)
    controls.pack(fill=tk.X, pady=(0, 10))

    status_var = tk.StringVar(value="Status: Idle")

    main = ttk.Frame(container)
    main.pack(fill=tk.BOTH, expand=True)

    video_canvas = tk.Canvas(main, width=800, height=600, bg="black", highlightthickness=0)
    video_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    side_panel = ttk.LabelFrame(main, text="Obiecte Detectate", padding=10)
    side_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

    detected_text = tk.Text(side_panel, width=28, height=34, state=tk.DISABLED)
    detected_text.pack(fill=tk.BOTH, expand=True)

    hint = ttk.Label(
        side_panel,
        text="Prima rulare poate dura mai mult\n(downloadeaza modelul YOLO).",
        justify=tk.LEFT,
    )
    hint.pack(anchor="w", pady=(8, 0))

    start_btn = ttk.Button(controls, text="Start Camera", command=start_camera)
    start_btn.pack(side=tk.LEFT)

    stop_btn = ttk.Button(controls, text="Stop Camera", command=stop_camera, state=tk.DISABLED)
    stop_btn.pack(side=tk.LEFT, padx=8)

    status_label = ttk.Label(controls, textvariable=status_var)
    status_label.pack(side=tk.LEFT, padx=12)

    root.protocol("WM_DELETE_WINDOW", on_close)


def ensure_model_loaded():
    global model

    if model is not None:
        return True

    status_var.set("Status: Incarc modelul YOLO...")
    root.update_idletasks()

    try:
        model = YOLO(str(MODEL_PATH))
        return True
    except Exception as exc:
        model = None
        status_var.set("Status: Eroare model YOLO")
        messagebox.showerror(
            "YOLO Error",
            "Nu am putut incarca modelul YOLO.\n\n"
            f"Locatie asteptata: {MODEL_PATH}\n"
            "La prima rulare, fisierul se downloadeaza automat.\n"
            "Daca downloadul esueaza, verifica internetul sau copiaza manual `yolov8n.pt` langa acest script.\n\n"
            f"Detalii: {exc}",
        )
        return False


def update_detected_objects(result):
    names = result.names
    classes = result.boxes.cls.tolist() if result.boxes is not None else []

    counter = Counter()
    for cls_id in classes:
        class_id = int(cls_id)
        if isinstance(names, dict):
            label = names.get(class_id, f"class_{class_id}")
        else:
            if class_id < len(names):
                label = names[class_id]
            else:
                label = f"class_{class_id}"
        counter[label] += 1

    lines = ["Detectii curente:"]
    if counter:
        for name, count in counter.most_common():
            lines.append(f"- {name}: {count}")
    else:
        lines.append("- (nimic detectat)")

    detected_text.configure(state=tk.NORMAL)
    detected_text.delete("1.0", tk.END)
    detected_text.insert(tk.END, "\n".join(lines))
    detected_text.configure(state=tk.DISABLED)


def render_frame(frame_bgr):
    global last_photo

    frame_rgb = cv.cvtColor(frame_bgr, cv.COLOR_BGR2RGB)
    frame_rgb = cv.resize(frame_rgb, (800, 600))
    image = Image.fromarray(frame_rgb)
    last_photo = ImageTk.PhotoImage(image=image)

    video_canvas.delete("all")
    video_canvas.create_image(0, 0, image=last_photo, anchor=tk.NW)


def update_frame():
    global running, capture

    if not running or capture is None:
        return

    ok, frame_bgr = capture.read()
    if not ok:
        status_var.set("Status: Eroare frame camera")
        stop_camera()
        return

    result = model.predict(frame_bgr, conf=CONF_THRESHOLD, verbose=False)[0]
    frame_annotated = result.plot()

    update_detected_objects(result)
    render_frame(frame_annotated)

    root.after(UPDATE_MS, update_frame)


def start_camera():
    global running, capture

    if running:
        return

    if not ensure_model_loaded():
        return

    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        capture = None
        messagebox.showerror("Camera Error", "Nu pot deschide camera (index 0).")
        return

    running = True
    start_btn.configure(state=tk.DISABLED)
    stop_btn.configure(state=tk.NORMAL)
    status_var.set("Status: Running")
    update_frame()


def stop_camera():
    global running, capture

    running = False
    start_btn.configure(state=tk.NORMAL)
    stop_btn.configure(state=tk.DISABLED)
    status_var.set("Status: Stopped")

    if capture is not None:
        capture.release()
        capture = None


def on_close():
    stop_camera()
    root.destroy()


def main():
    build_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
