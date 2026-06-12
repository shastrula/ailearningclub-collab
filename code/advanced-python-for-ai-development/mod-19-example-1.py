import json

class ModelRegistry:
    def __init__(self, registry_path):
        self.registry_path = registry_path
        self.registry = self.load_registry()
    
    def register(self, model_id, version, metadata):
        self.registry[f'{model_id}:{version}'] = {
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata
        }
        self.save_registry()
    
    def load_registry(self):
        if os.path.exists(self.registry_path):
            with open(self.registry_path) as f:
                return json.load(f)
        return {}
    
    def save_registry(self):
        with open(self.registry_path, 'w') as f:
            json.dump(self.registry, f)