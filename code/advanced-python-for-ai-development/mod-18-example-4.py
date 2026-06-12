class ModelMonitor:
    def __init__(self):
        self.predictions = []
        self.actuals = []
    
    def update(self, pred, actual):
        self.predictions.append(pred)
        self.actuals.append(actual)
    
    def accuracy(self):
        return np.mean(
            np.array(self.predictions) == np.array(self.actuals)
        )
    
    def alert_if_degraded(self, threshold=0.95):
        if self.accuracy() < threshold:
            logger.error('Performance degraded', accuracy=self.accuracy())