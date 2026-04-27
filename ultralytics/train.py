from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark



if __name__ == "__main__":
    models = ["yolo26s.pt", "yolo26m.pt", "yolo26l.pt"]

    for model_name in models:
        model = YOLO(model_name)

        model.train(data="african-wildlife.yaml", epochs=100, imgsz=640, device=0, name=model_name)
