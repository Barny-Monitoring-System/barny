from psutil import virtual_memory


class Swap:
    def total(self):
        return virtual_memory()[0]

    def used(self):
        return virtual_memory()[1]

    def percent(self):
        return virtual_memory()[3]

    def metrics(self):
        return {
            "swap": {
                "total": self.total(),
                "used": self.used(),
                "percent": self.percent(),
            }
        }