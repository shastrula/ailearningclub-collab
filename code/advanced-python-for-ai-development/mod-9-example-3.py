from typing import Generic, TypeVar

T = TypeVar('T')

class ModelRegistry(Generic[T]):
    def __init__(self):
        self.models: dict[str, T] = {}
    
    def register(self, name: str, model: T) -> None:
        self.models[name] = model
    
    def get(self, name: str) -> T:
        return self.models[name]