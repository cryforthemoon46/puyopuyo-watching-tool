import cv2.cv2
import numpy as np

from config import *
from src.score import Score

YMIN = 886
YMAX = 936
XMIN = {PLAYER1: 353, PLAYER2: 1251}
XMAX = {PLAYER1: 673, PLAYER2: 1571}


def create_score(frame: np.ndarray, player: int) -> Score:
    img = frame[YMIN:YMAX, XMIN[player]:XMAX[player]]
    return Score(img)
