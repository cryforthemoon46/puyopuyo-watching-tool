import math


class OjamaRateObserver:
    def __init__(self):
        self._ojama_rate = 1.0
        self.export()

    def forward(self, ojama_rate):
        if ojama_rate == self._ojama_rate:
            return
        self._ojama_rate = math.floor(ojama_rate * 100) / 100
        self.export()

    def export(self):
        with open('./text_files/ojama_rate.txt', 'w', encoding='UTF-8') as f:
            f.write(f'×{self._ojama_rate:.2f}')
