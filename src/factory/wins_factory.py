import cv2
import numpy as np

from config import *
from src.service import calc_zncc

TEMPLATE_DIGITS = {
    '0': cv2.imread('./assets/wins/0.png'),
    '1': cv2.imread('./assets/wins/1.png'),
    '2': cv2.imread('./assets/wins/2.png'),
    '3': cv2.imread('./assets/wins/3.png'),
    '4': cv2.imread('./assets/wins/4.png'),
    '5': cv2.imread('./assets/wins/5.png'),
    '6': cv2.imread('./assets/wins/6.png'),
    '7': cv2.imread('./assets/wins/7.png'),
    '8': cv2.imread('./assets/wins/8.png'),
    '9': cv2.imread('./assets/wins/9.png')
}
YMIN = 970
YMAX = 1006
XMIN1 = {PLAYER1: 810, PLAYER2: 1057}
XMAX1 = {PLAYER1: 836, PLAYER2: 1083}
XMIN2 = {PLAYER1: 837, PLAYER2: 1084}
XMAX2 = {PLAYER1: 863, PLAYER2: 1110}


def create_wins(frame: np.ndarray, player: int) -> int:
    wins = img2str(frame[YMIN:YMAX, XMIN1[player]: XMAX1[player]]) + \
           img2str(frame[YMIN:YMAX, XMIN2[player]: XMAX2[player]])
    if not len(wins):
        return -1
    return int(wins)


def img2str(img: np.ndarray) -> str:
    max_zncc = 0.5
    tmp_num = ''
    for num, tpl_img in TEMPLATE_DIGITS.items():
        zncc = calc_zncc(img, tpl_img)
        if zncc > max_zncc:
            max_zncc = zncc
            tmp_num = num
    return tmp_num
