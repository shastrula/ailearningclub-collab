# Linear Algebra in Code: Tensors & Vectorization

**Duration:** 15 min

## Overview

Linear Algebra in Code: Tensors & Vectorization is a critical component of maths-and-statistics-in-ai that professionals encounter regularly in production systems.

## Core Concepts

Understanding Linear Algebra in Code: Tensors & Vectorization requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Linear Algebra in Code: Tensors & Vectorization connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Linear Algebra in Code: Tensors & Vectorization effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Linear Algebra in Code: Tensors & Vectorization in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Linear Algebra in Code: Tensors & Vectorization behaves differently at scale
- **Mission-Critical Applications** - Different tradeoffs when failures are expensive

## Common Mistakes

Learning from others' experiences:
- Insufficient planning before implementation
- Over-optimization before identifying real bottlenecks
- Inadequate error handling in production
- Lack of monitoring for degradation

## Best Practices

- Measure before you optimize
- Start simple and add complexity only when needed
- Document your design decisions for future maintainers
- Build observability into systems from the start
- Plan for maintenance and operational updates


## Code Examples

```python
import time
import numpy as np

# Representing 1000 tokens, each with 768 dimensions (like BERT embeddings)
tokens = np.random.randn(1000, 768)
weights = np.random.randn(768, 768)

# Pure Python loop (DON'T DO THIS)
def slow_matmul(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

start = time.time()
# This would take ~30 seconds for 1000x768 matrices
# slow_result = slow_matmul(tokens, weights)
print("Pure Python: ~30 seconds (skipped)")
```

```python
# NumPy vectorized (FAST)
start = time.time()
result = np.matmul(tokens, weights)  # or tokens @ weights
elapsed = time.time() - start
print(f"NumPy: {elapsed:.4f} seconds")  # ~0.01 seconds

# PyTorch on GPU (EVEN FASTER)
import torch
tokens_gpu = torch.randn(1000, 768, device="cuda")
weights_gpu = torch.randn(768, 768, device="cuda")

start = time.time()
result_gpu = torch.matmul(tokens_gpu, weights_gpu)
elapsed = time.time() - start
print(f"PyTorch GPU: {elapsed:.4f} seconds")  # ~0.001 seconds
```

```python
# Manual implementation (for understanding)
def matmul_manual(A, B):
    m, n = A.shape
    n, p = B.shape
    C = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            C[i, j] = np.dot(A[i, :], B[:, j])  # Dot product of row i and column j
    return C

# Verify it matches NumPy
A = np.random.randn(3, 4)
B = np.random.randn(4, 5)
assert np.allclose(matmul_manual(A, B), A @ B)
```

```python
import torch
import torch.nn.functional as F

# Query embedding (768-dim, like from a BERT encoder)
query = torch.randn(768)

# Document embeddings (1000 documents, each 768-dim)
documents = torch.randn(1000, 768)

# Compute cosine similarity for all documents at once
# This is a single matrix multiplication!
similarities = F.cosine_similarity(query.unsqueeze(0), documents)

# Get top-5 most similar documents
top_5_indices = torch.topk(similarities, k=5).indices
print(f"Most similar documents: {top_5_indices}")
```

```python
import torch
import time

# Test on Apple Silicon GPU
device = "mps" if torch.backends.mps.is_available() else "cpu"

A = torch.randn(4096, 4096, device=device)
B = torch.randn(4096, 4096, device=device)

start = time.time()
C = torch.matmul(A, B)
elapsed = time.time() - start

print(f"4096x4096 matmul on {device}: {elapsed:.4f}s")
# MPS: ~0.05s | CPU: ~2s
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/maths-and-statistics-in-ai/mod-1.ipynb)

