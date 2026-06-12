import pickle
import hashlib

def save_model(model, path, metadata=None):
    model_bytes = pickle.dumps(model)
    model_hash = hashlib.sha256(model_bytes).hexdigest()
    
    artifact = {
        'model': model_bytes,
        'hash': model_hash,
        'metadata': metadata or {},
        'timestamp': datetime.now().isoformat()
    }
    
    with open(path, 'wb') as f:
        pickle.dump(artifact, f)
    
    return model_hash