from ultralytics import YOLO

model = YOLO('yolov9/yolov8n.pt')

results = model.train(data='data.yaml', epochs=6, cfg='config.yaml')

