# Parametric vs Non-parametric Tests

**Duration:** 15 min

## Overview

Parametric vs Non-parametric Tests is a critical component of statistics-for-ml that professionals encounter regularly in production systems.

## Core Concepts

Understanding Parametric vs Non-parametric Tests requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Parametric vs Non-parametric Tests connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Parametric vs Non-parametric Tests effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Parametric vs Non-parametric Tests in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Parametric vs Non-parametric Tests behaves differently at scale
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

Non-parametric tests do not assume a specific distribution for the data. They are useful when the data does not meet the assumptions of parametric tests, such as normality. Examples include the Mann-Whitney U test and the Kruskal-Wallis test.

```python title="example2.py"
import scipy.stats as stats

# Sample data
data1 = [5, 7, 8, 6, 7]
data2 = [6, 8, 9, 7, 8]

# Perform Mann-Whitney U test
u_stat, p_value = stats.mannwhitneyu(data1, data2)

print(f'U-statistic: {u_stat}')
print(f'P-value: {p_value}')
```

> **💡 Tip:** Always check the assumptions of your data before choosing between parametric and non-parametric tests. Misapplying these tests can lead to incorrect conclusions.

Non-parametric tests do not assume a specific distribution for the data. They are useful when the data does not meet the assumptions of parametric tests, such as normality. Examples include the Mann-Whitney U test and the Kruskal-Wallis test.

```python title="example2.py"
import scipy.stats as stats

# Sample data
data1 = [5, 7, 8, 6, 7]
data2 = [6, 8, 9, 7, 8]

# Perform Mann-Whitney U test
u_stat, p_value = stats.mannwhitneyu(data1, data2)

print(f'U-statistic: {u_stat}')
print(f'P-value: {p_value}')
```

>
  <p class="font-semibold mb-3">❓ Which test assumes the data follows a specific distribution?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387121152" value="0">
      <span>Mann-Whitney U test</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387121152" value="1">
      <span>Kruskal-Wallis test</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387121152" value="2">
      <span>t-test</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387121152" value="3">
      <span>Chi-square test</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Non-parametric tests do not assume a specific distribution for the data. They are useful when the data does not meet the assumptions of parametric tests, such as normality. Examples include the Mann-Whitney U test and the Kruskal-Wallis test.

```python title="example2.py"
import scipy.stats as stats

# Sample data
data1 = [5, 7, 8, 6, 7]
data2 = [6, 8, 9, 7, 8]

# Perform Mann-Whitney U test
u_stat, p_value = stats.mannwhitneyu(data1, data2)

print(f'U-statistic: {u_stat}')
print(f'P-value: {p_value}')
```

>
  <p class="font-semibold mb-3">❓ Which test does not assume a specific distribution for the data?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387120896" value="0">
      <span>t-test</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387120896" value="1">
      <span>ANOVA</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387120896" value="2">
      <span>Mann-Whitney U test</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387120896" value="3">
      <span>Pearson's correlation</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/statistics-for-ml/mod-6.ipynb)

