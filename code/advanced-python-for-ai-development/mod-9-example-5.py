from typing import Optional

def load_model(path: str) -> Optional[Model]:
    if not os.path.exists(path):
        return None
    return Model.load(path)

# Type checking catches: model.predict() without None check