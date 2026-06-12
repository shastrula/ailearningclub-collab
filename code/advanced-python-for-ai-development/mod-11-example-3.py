import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name}: {elapsed:.4f}s")

with timer("feature_extraction"):
    features = extract_features(X)