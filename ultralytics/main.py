import cv2
import time
from ultralytics import YOLO


def find_working_camera(camera_indexes=(0, 1), attempts_per_camera=5):
    for index in camera_indexes:
        print(f"Checking camera index {index}...")

        cap = cv2.VideoCapture(index, cv2.CAP_V4L2)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)

        for attempt in range(attempts_per_camera):
            if cap.isOpened():
                ret, frame = cap.read()

                if ret and frame is not None:
                    print(f"Using camera index {index}")
                    return index, cap

            print(f"Camera {index} not ready, attempt {attempt + 1}/{attempts_per_camera}")
            time.sleep(1)

        cap.release()

    raise RuntimeError("No working camera found on index 0 or 1")


model = YOLO("/home/teamrhino/Model-Training/ultralytics/yolov8m.engine")

camera_index, cap = find_working_camera((0, 1))

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("Failed to read frame. Trying to reconnect...")

        cap.release()
        time.sleep(2)

        camera_index, cap = find_working_camera((0, 1))
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