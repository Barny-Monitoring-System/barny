from psutil import virtual_memory


class Ram:
    def total(self):
        return virtual_memory()[0]

    def used(self):
        return virtual_memory()[3]

    def percent(self):
        return virtual_memory()[2]

    def metrics(self):
        return {
            "ram": {
                "total": self.total(),
                "used": self.used(),
                "percent": self.percent(),
            }
        }
