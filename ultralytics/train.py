from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model.train(data="african-wildlife.yaml", epochs=100, imgsz=640, device=0)