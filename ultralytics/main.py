from ultralytics import YOLO

model = YOLO("rtdetr-l.pt")

model.track(source="https://www.youtube.com/watch?v=OwhFk1go2nk", show=True, tracker="bytetrack.yaml")