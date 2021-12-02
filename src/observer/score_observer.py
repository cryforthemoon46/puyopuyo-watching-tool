class ScoreObserver:
    def __init__(self):
        self._score = [0, 0]

    @property
    def is_start(self) -> bool:
        if self._score[-2] == 0 and self._score[-1] > 0:
            return True
        return False

    def forward(self, score: int) -> None:
        if score < 0:
            return
        self._score.append(score)
        self._score = self._score[-2:]
