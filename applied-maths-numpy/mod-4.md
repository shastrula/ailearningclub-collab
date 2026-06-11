# Probability and Random Numbers

**Duration:** 15 min

## Overview

Probability and Random Numbers is a critical component of applied-maths-numpy that professionals encounter regularly in production systems.

## Core Concepts

Understanding Probability and Random Numbers requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Probability and Random Numbers connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Probability and Random Numbers effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Probability and Random Numbers in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Probability and Random Numbers behaves differently at scale
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

# Set seed for reproducibility
np.random.seed(42)

# Uniform distribution [0, 1)
uniform = np.random.rand(5)

# Normal distribution (mean=0, std=1)
normal = np.random.randn(5)

# Random integers
integers = np.random.randint(0, 10, 5)

# Random choice from array
choices = np.random.choice([1, 2, 3, 4, 5], 5)
```

```python
# Uniform distribution
uniform_samples = np.random.uniform(0, 10, 1000)

# Normal distribution
normal_samples = np.random.normal(loc=0, scale=1, size=1000)

# Binomial distribution
binomial_samples = np.random.binomial(n=10, p=0.5, size=1000)

# Poisson distribution
poisson_samples = np.random.poisson(lam=3, size=1000)
```

```python
# Simulate coin flips
flips = np.random.randint(0, 2, 10000)

# Probability of heads
p_heads = np.sum(flips) / len(flips)
print(f"P(Heads) ≈ {p_heads}")  # ≈ 0.5

# Simulate dice rolls
rolls = np.random.randint(1, 7, 10000)

# Probability of rolling 6
p_six = np.sum(rolls == 6) / len(rolls)
print(f"P(6) ≈ {p_six}")  # ≈ 0.167
```

```python
# Generate samples
samples = np.random.normal(loc=5, scale=2, size=10000)

# Expected value (mean)
expected_value = np.mean(samples)
print(f"E[X] ≈ {expected_value}")  # ≈ 5

# Variance
variance = np.var(samples)
print(f"Var(X) ≈ {variance}")  # ≈ 4

# Standard deviation
std_dev = np.std(samples)
print(f"σ ≈ {std_dev}")  # ≈ 2
```

```python
# Estimate π using Monte Carlo
n_samples = 100000

# Generate random points in [0,1] x [0,1]
x = np.random.uniform(0, 1, n_samples)
y = np.random.uniform(0, 1, n_samples)

# Distance from origin
distances = np.sqrt(x**2 + y**2)

# Points inside unit circle
inside_circle = np.sum(distances <= 1)

# Estimate π
pi_estimate = 4 * inside_circle / n_samples
print(f"π ≈ {pi_estimate}")  # ≈ 3.14159
```


## Quiz

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What does np.random.randn() generate?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5555555555" value="0">
      <span>Random integers</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5555555555" value="1">
      <span>Samples from standard normal distribution</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5555555555" value="2">
      <span>Uniform random numbers</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5555555555" value="3">
      <span>Random boolean values</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/applied-maths-numpy/mod-4.ipynb)

