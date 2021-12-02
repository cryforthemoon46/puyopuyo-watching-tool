from config import *


class WinsObserver:
    def __init__(self):
        self._player1_wins = 0
        self._player2_wins = 0
        self._player1_consecutive_wins = 0
        self._player2_consecutive_wins = 0
        self.is_finish = False

    def forward(self, player1_wins: int, player2_wins: int) -> None:
        is_player1_win = player1_wins - self._player1_wins == 1
        is_player2_win = player2_wins - self._player2_wins == 1
        self.is_finish = is_player1_win + is_player2_win == 1

        self._player1_wins = player1_wins
        self._player2_wins = player2_wins

        if is_player1_win:
            self._player1_consecutive_wins += 1
            self._player2_consecutive_wins = 0
        if is_player2_win:
            self._player1_consecutive_wins = 0
            self._player2_consecutive_wins += 1

    def export(self):
        with open('./text_files/player1_consecutive_wins.txt', 'w',
                  encoding='UTF-8') as f:
            f.write(f'{self._player1_consecutive_wins}連勝')
        with open('./text_files/player2_consecutive_wins.txt', 'w',
                  encoding='UTF-8') as f:
            f.write(f'{self._player2_consecutive_wins}連勝')

    def reset(self):
        self._player1_consecutive_wins = 0
        self._player2_consecutive_wins = 0
        self.export()
