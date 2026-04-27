from ultralytics.utils.benchmarks import benchmark


if __name__ == '__main__':
    root_path = "C:\\Users\\patri\\Github\\Model-Training\\ultralytics\\runs\\detect\\"

    benchmark(model=root_path + "rtdetr-l\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640)
    benchmark(model=root_path + "yolo26n\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640)
    benchmark(model=root_path + "yolo26s\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640)
    benchmark(model=root_path + "yolo26m\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640)
    benchmark(model=root_path + "yolo26l\\weights\\best.pt", data="african-wildlife.yaml", imgsz=640)
