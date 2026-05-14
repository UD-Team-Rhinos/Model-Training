import cv2
import time
from ultralytics import YOLO

CAMERA_INDEX = 0

model = YOLO("/home/teamhnj/Model-Training/ultralytics/yolov8.engine")
# or:
# model = YOLO("/home/teamhnj/Model-Training/ultralytics/yolov8n.pt")

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

for attempt in range(20):
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print("Camera ready")
            break

    print("Waiting for camera...")
    time.sleep(2)
else:
    raise RuntimeError("Camera not found or not ready")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        time.sleep(0.1)
        continue

    results = model.track(
        frame,
        device=0,
        persist=True,
        tracker="bytetrack.yaml",
        imgsz=640,
        conf=0.25,
        classes=[0],
        verbose=False
    )

    annotated = results[0].plot()

    cv2.imshow("YOLO Tracking", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()