from numba import jit

@jit(nopython=True)
def compute_distances(X):
    distances = np.zeros((X.shape[0], X.shape[0]))
    for i in range(X.shape[0]):
        for j in range(i+1, X.shape[0]):
            distances[i, j] = np.sqrt(np.sum((X[i] - X[j])**2))
    return distances

# First call JIT compiles, subsequent calls are ~100x faster