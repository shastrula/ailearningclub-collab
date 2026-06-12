from typing import Protocol

class Predictor(Protocol):
    def predict(self, X: np.ndarray) -> np.ndarray: ...
    def fit(self, X: np.ndarray, y: np.ndarray) -> None: ...

def evaluate_model(model: Predictor, X_test: np.ndarray):
    return model.predict(X_test)