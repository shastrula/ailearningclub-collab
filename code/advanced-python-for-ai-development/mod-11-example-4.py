import numpy as np

# Slow: loops
result = []
for x in data:
    result.append(x ** 2 + 2 * x + 1)

# Fast: vectorized
result = data ** 2 + 2 * data + 1  # 100x faster