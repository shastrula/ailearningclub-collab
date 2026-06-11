# Calculus Operations with NumPy

**Duration:** 15 min

## Overview

Calculus Operations with NumPy is a critical component of applied-maths-numpy that professionals encounter regularly in production systems.

## Core Concepts

Understanding Calculus Operations with NumPy requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Calculus Operations with NumPy connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Calculus Operations with NumPy effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Calculus Operations with NumPy in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Calculus Operations with NumPy behaves differently at scale
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
import numpy as np

# Approximate derivative using finite differences
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example: f(x) = x²
def f(x):
    return x**2

# Derivative at x=3 should be 6
print(derivative(f, 3))  # ≈ 6.0
```

```python
# Compute gradient of a function
x = np.array([1.0, 2.0, 3.0])

# Function: f(x, y, z) = x² + y² + z²
def f(x):
    return np.sum(x**2)

# Numerical gradient
def numerical_gradient(f, x, h=1e-5):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_h = x.copy()
        x_h[i] += h
        grad[i] = (f(x_h) - f(x)) / h
    return grad

grad = numerical_gradient(f, x)
print("Gradient:", grad)  # [2, 4, 6]
```

```python
# Trapezoidal rule for integration
def trapezoidal_integration(f, a, b, n=1000):
    x = np.linspace(a, b, n)
    y = f(x)
    dx = (b - a) / n
    return np.sum((y[:-1] + y[1:]) / 2) * dx

# Example: integrate x² from 0 to 1
def f(x):
    return x**2

result = trapezoidal_integration(f, 0, 1)
print("Integral:", result)  # ≈ 0.333 (exact: 1/3)
```

```python
# Simple gradient descent
def gradient_descent(f, grad_f, x0, learning_rate=0.01, iterations=100):
    x = x0.copy()
    for i in range(iterations):
        grad = grad_f(x)
        x = x - learning_rate * grad
    return x

# Example: minimize f(x) = (x-3)²
def f(x):
    return (x - 3)**2

def grad_f(x):
    return 2 * (x - 3)

x_min = gradient_descent(f, grad_f, x0=0.0)
print("Minimum at x =", x_min)  # ≈ 3.0
```

```python
# Compute partial derivatives
def partial_derivative(f, x, i, h=1e-5):
    x_h = x.copy()
    x_h[i] += h
    return (f(x_h) - f(x)) / h

# Example: f(x, y) = x² + xy + y²
def f(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2

x = np.array([1.0, 2.0])
df_dx = partial_derivative(f, x, 0)  # ∂f/∂x
df_dy = partial_derivative(f, x, 1)  # ∂f/∂y

print("∂f/∂x =", df_dx)  # ≈ 4
print("∂f/∂y =", df_dy)  # ≈ 5
```


## Quiz

<div class="quiz">
  <p class="font-semibold mb-3">❓ What does gradient descent do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4444444444" value="0">
      <span>Finds minimum by moving in direction of negative gradient</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4444444444" value="1">
      <span>Computes the derivative of a function</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4444444444" value="2">
      <span>Integrates a function</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4444444444" value="3">
      <span>Solves linear equations</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/applied-maths-numpy/mod-3.ipynb)

