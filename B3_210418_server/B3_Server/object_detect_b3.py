# -*- coding: utf-8 -*-

from pydarknet import Detector, Image
import cv2

class Object_Detection():
    def __init__(self):
        self.net = Detector(bytes("yolov4_bear.cfg", encoding="utf-8"),
                            bytes("yolov4_bear.weights", encoding="utf-8"),
                            0,
                            bytes("bear.data", encoding="utf-8"))

    def Detection(self, img):
        cv2.imshow(Image(img))
        results = self.net.detect(Image(img))
        detect_list = []
        print(results)

        for cat, score, bounds in results:
            x, y, w, h = bounds
            cv2.rectangle(img,
                          (int(x - w / 2), int(y - h / 2)),
                          (int(x + w / 2), int(y + h / 2)),
                          (255, 0, 0),
                          thickness=2)
            cv2.putText(img,
                        str(cat.decode("utf-8")),
                        (int(x - w / 2), int(y + h / 4)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
            detect_list.append(cat.decode())

        cv2.imshow('dect', img)
        self.object = detect_list