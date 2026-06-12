from contextlib import contextmanager

@contextmanager
def gpu_context(device_id):
    torch.cuda.set_device(device_id)
    try:
        yield torch.cuda.current_device()
    finally:
        torch.cuda.empty_cache()

with gpu_context(0) as device:
    model.to(device)
    predictions = model(X)