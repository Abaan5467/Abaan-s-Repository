import cv2
import mediapipe
import time


cam = cv2.VideoCapture(0)

mphand = mediapipe.solutions.hands
hands = mphand.Hands()
handsdraw = mediapipe.solutions.drawing_utils


while True:
    frame,img = cam.read()
    img = cv2.flip(img,1)
    rgbimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(rgbimg)
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handloc in result.multi_hand_landmarks:
            handsdraw.draw_landmarks(img,handloc,mphand.HAND_CONNECTIONS)

    cv2.imshow('Camera',img)
    cv2.waitKey(1)