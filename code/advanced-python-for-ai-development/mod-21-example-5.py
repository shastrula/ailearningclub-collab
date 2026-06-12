class ModelRollback:
    def __init__(self):
        self.current = load_model('v5')
        self.previous = load_model('v4')
    
    def switch_to_previous(self):
        self.current, self.previous = self.previous, self.current
        log_event('switched_to_v4')
    
    def predict(self, X):
        return self.current.predict(X)