# Statistical Analysis with NumPy

**Duration:** 15 min

## Overview

Statistical Analysis with NumPy is a critical component of applied-maths-numpy that professionals encounter regularly in production systems.

## Core Concepts

Understanding Statistical Analysis with NumPy requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Statistical Analysis with NumPy connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Statistical Analysis with NumPy effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Statistical Analysis with NumPy in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Statistical Analysis with NumPy behaves differently at scale
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

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean (average)
mean = np.mean(data)  # 5.5

# Median (middle value)
median = np.median(data)  # 5.5

# Mode (most frequent) - use scipy
from scipy import stats
mode = stats.mode(data)[0]  # 1 (or any value, all appear once)

# Standard deviation
std = np.std(data)  # ≈ 2.87

# Variance
var = np.var(data)  # ≈ 8.25

# Min and max
min_val = np.min(data)  # 1
max_val = np.max(data)  # 10

# Range
range_val = max_val - min_val  # 9
```

```python
data = np.random.normal(100, 15, 1000)

# Percentiles
p25 = np.percentile(data, 25)  # 25th percentile
p50 = np.percentile(data, 50)  # 50th percentile (median)
p75 = np.percentile(data, 75)  # 75th percentile

# Quantiles
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)

# Interquartile range
iqr = q3 - q1
```

```python
# Compare two samples
sample1 = np.random.normal(100, 15, 100)
sample2 = np.random.normal(105, 15, 100)

# T-test
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(sample1, sample2)

print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

# If p-value < 0.05, samples are significantly different
```

```python
# Generate correlated data
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Pearson correlation
from scipy.stats import pearsonr
corr, p_value = pearsonr(x, y)

print(f"Correlation: {corr}")  # ≈ 0.87
print(f"p-value: {p_value}")
```

```python
# Simple linear regression
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Fit line: y = mx + b
coefficients = np.polyfit(x, y, 1)
m, b = coefficients

print(f"Slope: {m}")
print(f"Intercept: {b}")

# Predictions
y_pred = m * x + b

# R-squared
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R²: {r_squared}")
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/applied-maths-numpy/mod-5.ipynb)

