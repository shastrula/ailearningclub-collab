class ModelError(Exception):
    pass

class DataValidationError(ModelError):
    pass

class PredictionError(ModelError):
    pass

try:
    if not validate_data(X):
        raise DataValidationError("Invalid features")
except DataValidationError as e:
    logger.error(f"Data error: {e}")
    handle_gracefully()