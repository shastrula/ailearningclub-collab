# INT4 and INT8 Quantization

**Duration:** 15 min

## Overview

INT4 and INT8 Quantization is a critical component of quantization-engineering that professionals encounter regularly in production systems.

## Core Concepts

Understanding INT4 and INT8 Quantization requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where INT4 and INT8 Quantization connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing INT4 and INT8 Quantization effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply INT4 and INT8 Quantization in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - INT4 and INT8 Quantization behaves differently at scale
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

INT8 quantization is a widely-used technique that converts floating-point weights and activations to 8-bit integers. This method strikes a balance between model size reduction and performance, making it suitable for various deployment scenarios. The quantization process involves determining a scale factor and zero-point for each tensor to maintain accuracy.

```python title="example2.py"
import numpy as np

# Example weights
weights_fp32 = np.array([1.2, -0.5, 0.8, -1.1], dtype=np.float32)

# Scaling factor
scale = np.max(np.abs(weights_fp32))

# Quantization to INT8
weights_int8 = np.round(weights_fp32 / scale * 127).astype(np.int8)

# Clipping to ensure values are within INT8 range
weights_int8 = np.clip(weights_int8, -128, 127)

print(weights_int8)
```

> **💡 Tip:** When performing quantization, ensure that the scale factor is chosen carefully to avoid overflow and underflow issues. Additionally, always test the quantized model to verify that it maintains acceptable performance levels.

INT8 quantization is a widely-used technique that converts floating-point weights and activations to 8-bit integers. This method strikes a balance between model size reduction and performance, making it suitable for various deployment scenarios. The quantization process involves determining a scale factor and zero-point for each tensor to maintain accuracy.

```python title="example2.py"
import numpy as np

# Example weights
weights_fp32 = np.array([1.2, -0.5, 0.8, -1.1], dtype=np.float32)

# Scaling factor
scale = np.max(np.abs(weights_fp32))

# Quantization to INT8
weights_int8 = np.round(weights_fp32 / scale * 127).astype(np.int8)

# Clipping to ensure values are within INT8 range
weights_int8 = np.clip(weights_int8, -128, 127)

print(weights_int8)
```

>
  <p class="font-semibold mb-3">❓ What is the primary purpose of INT4 quantization?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386948288" value="0">
      <span>To increase model accuracy</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386948288" value="1">
      <span>To reduce model size and computational cost</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386948288" value="2">
      <span>To improve training speed</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386948288" value="3">
      <span>To enhance model interpretability</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

INT8 quantization is a widely-used technique that converts floating-point weights and activations to 8-bit integers. This method strikes a balance between model size reduction and performance, making it suitable for various deployment scenarios. The quantization process involves determining a scale factor and zero-point for each tensor to maintain accuracy.

```python title="example2.py"
import numpy as np

# Example weights
weights_fp32 = np.array([1.2, -0.5, 0.8, -1.1], dtype=np.float32)

# Scaling factor
scale = np.max(np.abs(weights_fp32))

# Quantization to INT8
weights_int8 = np.round(weights_fp32 / scale * 127).astype(np.int8)

# Clipping to ensure values are within INT8 range
weights_int8 = np.clip(weights_int8, -128, 127)

print(weights_int8)
```

>
  <p class="font-semibold mb-3">❓ Which range does INT8 quantization clip values to ensure they fit within the INT8 format?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386947264" value="0">
      <span>-128 to 127</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386947264" value="1">
      <span>-256 to 255</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386947264" value="2">
      <span>0 to 255</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386947264" value="3">
      <span>-32 to 31</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/quantization-engineering/mod-6.ipynb)

