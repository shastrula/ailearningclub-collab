from contextlib import contextmanager

@contextmanager
def model_inference(model):
    try:
        yield model
    except Exception as e:
        logger.error(f"Inference failed: {e}")
        model.rollback()
    finally:
        model.cleanup()

with model_inference(my_model) as m:
    predictions = m.predict(X)