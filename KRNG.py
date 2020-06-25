import pafy
import cv2
import numpy as np
import hashlib as hl

url = 'https://www.youtube.com/watch?v=M5huFQWHyVI'

vPafy = pafy.new(url)
play = vPafy.getbest()

cap = cv2.VideoCapture(play.url)

ret, frame = cap.read()

print(int(hl.sha256(frame.data.tobytes()).hexdigest(), 16))

cap.release()