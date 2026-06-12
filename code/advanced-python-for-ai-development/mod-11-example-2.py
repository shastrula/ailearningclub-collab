from memory_profiler import profile

@profile
def train_model(X, y):
    features = extract_features(X)  # Line-level memory tracking
    model = Model()
    model.fit(features, y)
    return model

# Command: python -m memory_profiler train.py