from psutil import disk_usage


class Disk:
    def __init__(self, dir_to_check = "/"):
        self._dir_to_check = dir_to_check

    def total(self):
        return disk_usage(self._dir_to_check)[0]

    def used(self):
        return disk_usage(self._dir_to_check)[1]

    def percent(self):
        return disk_usage(self._dir_to_check)[3]

    def metrics(self):
        return {
            "disk": {
                "total": self.total(),
                "used": self.used(),
                "percent": self.percent(),
            }
        }
