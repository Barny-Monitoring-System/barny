from psutil import cpu_percent


class Cpu:
    def __init__(self, check_for_seconds):
        self._check_for_seconds = check_for_seconds

    def load(self):
        return cpu_percent(self._check_for_seconds)
