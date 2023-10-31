import cv2
import mediapipe
import os
import time


wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
#  --------------opening the webcam camera here--------------------//
while True:
    success, frame = cap.read()
    cv2.imshow("Image", frame)
    cv2.waitKey(1)
