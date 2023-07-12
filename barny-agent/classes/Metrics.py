class Metrics:
    def __init__(self, metric_sources: list):
        self._metric_sources = metric_sources

    def metrics(self):
        metrics = {}

        for source in self._metric_sources:
            metrics.update(source.metrics())

        return { "barny": metrics }
