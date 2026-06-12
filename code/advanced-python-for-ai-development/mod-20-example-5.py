import numpy as np

# Memory map large arrays
data = np.load('data.npy', mmap_mode='r')
# Array is on disk, accessed on-demand
subset = data[:1000]  # Only loads these rows