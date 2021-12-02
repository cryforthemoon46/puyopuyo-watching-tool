import time

import cv2
import numpy as np

from config import *
from src.factory import create_ojama_rate, create_score, create_wins
from src.observer import OjamaRateObserver, ScoreObserver, WinsObserver


def main():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FPS, 60)  # カメラFPSを60FPSに設定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # カメラ画像の横幅を1920に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # カメラ画像の縦幅を1080に設定

    ojama_rate_observer = OjamaRateObserver()
    score_observer = ScoreObserver()
    wins_observer = WinsObserver()
    wins_observer.export()

    begin_time = np.inf

    while True:
        _, frame = cap.read()

        player1_score = create_score(frame=frame, player=PLAYER1)
        player2_score = create_score(frame=frame, player=PLAYER2)

        # プレイヤー1のスコアが1以上になった瞬間を試合開始とする
        score_observer.forward(int(player1_score))
        if score_observer.is_start:
            begin_time = time.time()
            ojama_rate_observer = OjamaRateObserver()
        current_time = time.time()
        ojama_rate = create_ojama_rate(current_time - begin_time)
        ojama_rate_observer.forward(ojama_rate)

        player1_wins = create_wins(frame=frame, player=PLAYER1)
        player2_wins = create_wins(frame=frame, player=PLAYER2)
        if player1_wins < 0 or player2_wins < 0:
            continue
        wins_observer.forward(player1_wins, player2_wins)

        # 試合終了時の処理
        if not wins_observer.is_finish:
            continue
        begin_time = time.time()  # おじゃまレート初期化処理
        wins_observer.export()  # 連勝数を出力


if __name__ == '__main__':
    main()
