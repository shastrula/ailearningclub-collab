try:
    result = compute_features(X)
except ValueError as e:
    raise PredictionError("Failed to compute") from e

# Preserves original exception traceback