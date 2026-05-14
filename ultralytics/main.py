from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.track(source=0, device=0, show=True, tracker="bytetrack.yaml", persist=True, imgsz=1080, classes=[0])