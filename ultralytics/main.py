from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model.track("https://youtu.be/LNwODJXcvt4")