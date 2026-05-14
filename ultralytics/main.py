from ultralytics import YOLO
import time
import cv2

for attempt in range(20):
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        cap.release()
        if ret:
            print("Camera ready")
            break

    print("Waiting for camera...")
    time.sleep(2)
else:
    raise RuntimeError("Camera not found or not ready")

model = YOLO("yolov8s.engine")

model.track(source=0, device=0, show=True, tracker="bytetrack.yaml", persist=True, imgsz=1080, classes=[0])