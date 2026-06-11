# Resampling Methods: Bootstrap and Permutation Tests

**Duration:** 15 min

## Overview

Resampling Methods: Bootstrap and Permutation Tests is a critical component of statistics-for-ml that professionals encounter regularly in production systems.

## Core Concepts

Understanding Resampling Methods: Bootstrap and Permutation Tests requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Resampling Methods: Bootstrap and Permutation Tests connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Resampling Methods: Bootstrap and Permutation Tests effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Resampling Methods: Bootstrap and Permutation Tests in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Resampling Methods: Bootstrap and Permutation Tests behaves differently at scale
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


## Quiz

A Permutation Test is a non-parametric test that provides a way to assess the null hypothesis by comparing the observed test statistic to a distribution of test statistics obtained by randomly permuting the labels of the data. This method is useful for hypothesis testing when the assumptions of traditional parametric tests are violated.

```python title="permutation_test_example.py"
import numpy as np

# Sample data
group1 = np.array([1, 2, 3, 4, 5])
group2 = np.array([2, 3, 4, 5, 6])

# Observed difference in means
observed_diff = np.mean(group1) - np.mean(group2)

# Permutation test
n_permutations = 1000
permutation_diffs = []
for _ in range(n_permutations):
    combined = np.concatenate([group1, group2])
    np.random.shuffle(combined)
    permuted_group1 = combined[:len(group1)]
    permuted_group2 = combined[len(group1):]
    permutation_diffs.append(np.mean(permuted_group1) - np.mean(permuted_group2))

p_value = np.mean(np.abs(permutation_diffs) >= np.abs(observed_diff))
print(f'P-value: {p_value}')
```

> **💡 Tip:** Ensure that the number of bootstrap or permutation samples is sufficiently large to get a stable estimate of the statistic or p-value.

A Permutation Test is a non-parametric test that provides a way to assess the null hypothesis by comparing the observed test statistic to a distribution of test statistics obtained by randomly permuting the labels of the data. This method is useful for hypothesis testing when the assumptions of traditional parametric tests are violated.

```python title="permutation_test_example.py"
import numpy as np

# Sample data
group1 = np.array([1, 2, 3, 4, 5])
group2 = np.array([2, 3, 4, 5, 6])

# Observed difference in means
observed_diff = np.mean(group1) - np.mean(group2)

# Permutation test
n_permutations = 1000
permutation_diffs = []
for _ in range(n_permutations):
    combined = np.concatenate([group1, group2])
    np.random.shuffle(combined)
    permuted_group1 = combined[:len(group1)]
    permuted_group2 = combined[len(group1):]
    permutation_diffs.append(np.mean(permuted_group1) - np.mean(permuted_group2))

p_value = np.mean(np.abs(permutation_diffs) >
  <p class="font-semibold mb-3">❓ What is the primary purpose of the Bootstrap method?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387178880" value="0">
      <span>To perform hypothesis testing</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387178880" value="1">
      <span>To estimate statistics on a population by sampling a dataset with replacement</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387178880" value="2">
      <span>To visualize data distributions</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387178880" value="3">
      <span>To perform feature selection</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

A Permutation Test is a non-parametric test that provides a way to assess the null hypothesis by comparing the observed test statistic to a distribution of test statistics obtained by randomly permuting the labels of the data. This method is useful for hypothesis testing when the assumptions of traditional parametric tests are violated.

```python title="permutation_test_example.py"
import numpy as np

# Sample data
group1 = np.array([1, 2, 3, 4, 5])
group2 = np.array([2, 3, 4, 5, 6])

# Observed difference in means
observed_diff = np.mean(group1) - np.mean(group2)

# Permutation test
n_permutations = 1000
permutation_diffs = []
for _ in range(n_permutations):
    combined = np.concatenate([group1, group2])
    np.random.shuffle(combined)
    permuted_group1 = combined[:len(group1)]
    permuted_group2 = combined[len(group1):]
    permutation_diffs.append(np.mean(permuted_group1) - np.mean(permuted_group2))

p_value = np.mean(np.abs(permutation_diffs) >
  <p class="font-semibold mb-3">❓ What does a Permutation Test help to assess?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386913664" value="0">
      <span>The variance of a dataset</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386913664" value="1">
      <span>The null hypothesis by comparing the observed test statistic to a distribution of test statistics obtained by randomly permuting the labels of the data</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386913664" value="2">
      <span>The correlation between two variables</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386913664" value="3">
      <span>The accuracy of a machine learning model</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/statistics-for-ml/mod-17.ipynb)

