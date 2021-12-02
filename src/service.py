import cv2
import numpy as np

STANDARD_RATE = 70


def calc_zncc(roi_img: np.ndarray, tpl_img: np.ndarray) -> float:
    """
    :param roi_img: ぷよ画像
    :param tpl_img: テンプレート画像
    :return: 2つの画像の類似度 (ZNCC)
    """
    roi_h, roi_w = roi_img.shape[:2]
    roi_img = np.array(roi_img, dtype="float")
    roi_img -= np.mean(roi_img)

    tpl_img = cv2.resize(tpl_img, (roi_w, roi_h))
    tpl_img = np.array(tpl_img, dtype="float")
    tpl_img -= np.mean(tpl_img)

    numerator = np.sum(roi_img * tpl_img)
    denominator = np.sqrt(np.sum(roi_img ** 2)) * np.sqrt(
        np.sum(tpl_img ** 2))

    zncc = numerator / denominator if denominator != 0 else 0
    return zncc


def calc_margin(time):
    if time == np.nan or time < 96:
        return STANDARD_RATE / 70
    elif time < 112:
        return STANDARD_RATE / 52
    elif time < 128:
        return STANDARD_RATE / 34
    elif time < 144:
        return STANDARD_RATE / 25
    elif time < 160:
        return STANDARD_RATE / 16
    elif time < 176:
        return STANDARD_RATE / 12
    elif time < 192:
        return STANDARD_RATE / 8
    elif time < 208:
        return STANDARD_RATE / 6
    elif time < 224:
        return STANDARD_RATE / 4
    elif time < 240:
        return STANDARD_RATE / 3
    elif time < 256:
        return STANDARD_RATE / 2
    else:
        return STANDARD_RATE
