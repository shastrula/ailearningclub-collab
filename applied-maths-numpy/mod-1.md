# NumPy Basics and Arrays

**Duration:** 15 min

## Core Principles

NumPy Basics and Arrays builds on fundamental concepts that form the foundation of applied-maths-numpy. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering NumPy Basics and Arrays is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every applied-maths-numpy practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how NumPy Basics and Arrays connects to other components in applied-maths-numpy helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply NumPy Basics and Arrays in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement NumPy Basics and Arrays for their applied-maths-numpy system. They:
- Defined requirements clearly
- Chose an appropriate design pattern
- Implemented core functionality
- Added error handling and monitoring
- Deployed gradually to production

Their results demonstrate that following these principles leads to reliable systems.

## Common Challenges

Practitioners often encounter these issues:
- Underestimating complexity early on
- Insufficient testing before deployment
- Inadequate monitoring in production
- Not planning for future changes

Recognizing these patterns helps you avoid repeating them.

## Best Practices Summary

- Keep implementations simple until complexity is truly necessary
- Always measure before optimizing
- Document your design decisions for future maintainers
- Build monitoring into your system from the start
- Plan for updates and operational maintenance


## Code Examples

```python
import numpy as np

# 1D array (vector)
a = np.array([1, 2, 3])

# 2D array (matrix)
A = np.array([[1, 2], [3, 4]])

# Array of zeros
zeros = np.zeros((2, 3))

# Array of ones
ones = np.ones((2, 3))

# Range of values
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Random array
random_arr = np.random.rand(3, 3)
```

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(a + b)      # [5, 7, 9]
print(a * b)      # [4, 10, 18]
print(a / b)      # [0.25, 0.4, 0.5]

# Scalar operations
print(a * 2)      # [2, 4, 6]
print(a + 10)     # [11, 12, 13]
```

```python
A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.shape)    # (2, 3) - 2 rows, 3 columns
print(A.size)     # 6 - total elements
print(A.dtype)    # int64 - data type
print(A.ndim)     # 2 - number of dimensions
```

```python
a = np.array([10, 20, 30, 40, 50])

print(a[0])       # 10 - first element
print(a[-1])      # 50 - last element
print(a[1:4])     # [20, 30, 40] - elements 1 to 3
print(a[::2])     # [10, 30, 50] - every 2nd element
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/applied-maths-numpy/mod-1.ipynb)

