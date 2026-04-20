from ultralytics import YOLO

model = YOLO("yolo26n.pt")

model.track(source="https://youtu.be/LNwODJXcvt4", save=True, tracker="bytetrack.yaml")