from psutil import cpu_percent


class Cpu:
    def __init__(self, check_for_seconds = 1):
        self._check_for_seconds = check_for_seconds

    def percent(self):
        return cpu_percent(self._check_for_seconds)

    def metrics(self):
        return {
            "cpu": {
                "usage_percent": self.percent(),
            },
        }
