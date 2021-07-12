#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  WebcamModule.py
#
#  Copyright 2021 Alcides Fernando Tiago <alcidesft6@gmail.com>
#  MA 02110-1301, USA.
#
#


import cv2

cap = cv2.VideoCapture(0)


def getImg(display=False, size=[480, 240]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow('IMG', img)
    return img


if __name__ == '__main__':
    while True:
        img = getImg(True)
