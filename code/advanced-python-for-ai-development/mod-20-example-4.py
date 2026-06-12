class LazyModelLoader:
    def __init__(self, path):
        self.path = path
        self.model = None
    
    def get(self):
        if self.model is None:
            self.model = joblib.load(self.path)
        return self.model

loader = LazyModelLoader('model.pkl')
# Model only loads when accessed
predictions = loader.get().predict(X)