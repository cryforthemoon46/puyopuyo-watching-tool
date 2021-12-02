import cv2
import numpy as np

from src.service import calc_zncc

TEMPLATES = {
    '0': cv2.imread('./assets/score/0.png'),
    '1': cv2.imread('./assets/score/1.png'),
    '2': cv2.imread('./assets/score/2.png'),
    '3': cv2.imread('./assets/score/3.png'),
    '4': cv2.imread('./assets/score/4.png'),
    '5': cv2.imread('./assets/score/5.png'),
    '6': cv2.imread('./assets/score/6.png'),
    '7': cv2.imread('./assets/score/7.png'),
    '8': cv2.imread('./assets/score/8.png'),
    '9': cv2.imread('./assets/score/9.png'),
    'x': cv2.imread('./assets/score/x.png')
}
ZNCC_THRESHOLD = 0.5


class Score:
    def __init__(self, img: np.ndarray):
        self._str = img2str(img)

    def __int__(self):
        if self._str[4] != 'x':
            return int(self._str)
        return -1

    def __str__(self):
        return self._str

    @property
    def additional_score(self):
        if self._str[4] != 'x':
            return 0
        a, b = self._str.split('x')
        return int(a) * int(b)


def img2str(img: np.ndarray) -> str:
    tmp_str = ''
    for i in range(8):
        digit_img = img[:, i * 40: (i + 1) * 40]
        tmp_digit = '0'
        max_zncc = ZNCC_THRESHOLD
        for digit, tpl_img in TEMPLATES.items():
            zncc = calc_zncc(digit_img, tpl_img)
            if zncc > max_zncc:
                max_zncc = zncc
                tmp_digit = digit
        tmp_str += tmp_digit
    return tmp_str
