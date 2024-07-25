from ultralytics import YOLO
from PLDetect.yolov9 import detect_dual as detect
from ultralytics.utils.plotting import Annotator, colors
import os
import cv2


def run_and_detect(img_path):
    model = YOLO('/home/minhp/workspace/SmartSystem/Face/PLDetect/pl_detect/train3/weights/best.pt')
    names = model.names
    im0 = cv2.imread(img_path)
    results = model.predict(im0, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    annotator = Annotator(im0, line_width=2, example=names)

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])

            crop_obj = im0[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            cv2.imshow("ultralytics", crop_obj)
            cv2.waitKey(0)

    cv2.destroyAllWindows()
    return crop_obj
