import pafy
from cv2 import VideoCapture
import numpy as np
import hashlib as hl
import random

from KRNG import URL

def KRN():
    '''Get a Kitten Based Random Number'''
    vPafy = pafy.new(url=URL)
    play = vPafy.getbest()

    cap = VideoCapture(play.url)

    ret, frame = cap.read()
    number = int(hl.sha256(frame.data.tobytes()).hexdigest(), 16)
    cap.release()
    return number

def KPRNG() -> random.Random:
    '''Get a Kitten Seeded PRNG'''

    seed = KRN()
    rand = random.Random(seed)

    return rand