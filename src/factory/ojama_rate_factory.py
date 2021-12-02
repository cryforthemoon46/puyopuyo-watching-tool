CALIBRATION_TIME = 2
MARGIN_TIME = [96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256]
OJAMA_PUYO_RATE = [70, 52, 35, 26, 17, 13, 8, 6, 4, 3, 2]
STANDARD_RATE = 70


def create_ojama_rate(time: float) -> float:
    for margin_time, ojama_puyo_rate in zip(MARGIN_TIME, OJAMA_PUYO_RATE):
        if time < margin_time:
            return STANDARD_RATE / ojama_puyo_rate
    return STANDARD_RATE
