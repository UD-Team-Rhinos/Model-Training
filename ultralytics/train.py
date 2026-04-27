from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark



if __name__ == "__main__":
    # benchmark(model="C:\\Users\\patri\\Github\\Model-Training\\ultralytics\\runs\\detect\\yolo26n\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640, device=0)
    # benchmark(model="C:\\Users\\patri\\Github\\Model-Training\\ultralytics\\runs\\detect\\rtdetr-l\\weights\\best.pt", imgsz=640,device=0)

    models = ["rtdetr-x.pt"]

    for model_name in models:
        model = YOLO(model_name)

        model.train(data="african-wildlife.yaml", epochs=50, imgsz=640, device=0, name=model_name.replace(".pt", ""))
