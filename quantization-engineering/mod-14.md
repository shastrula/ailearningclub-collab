# Post-Training Quantization

**Duration:** 15 min

## Overview

Post-Training Quantization is a critical component of quantization-engineering that professionals encounter regularly in production systems.

## Core Concepts

Understanding Post-Training Quantization requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Post-Training Quantization connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Post-Training Quantization effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Post-Training Quantization in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Post-Training Quantization behaves differently at scale
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

Benchmarking is essential to evaluate the performance and efficiency gains of quantized models. It involves comparing the inference speed, memory usage, and accuracy of the quantized model against the original floating-point model to ensure that the quantization process has not adversely affected the model's performance.

```python title="example2.py"
import torch
import time

# Load original and quantized models
original_model = torch.hub.load('pytorch/vision:v0.10.0','mobilenet_v2', pretrained=True)
original_model.eval()
quantized_model = torch.quantization.quantize_dynamic(original_model, {torch.nn.Linear}, dtype=torch.qint8)

# Prepare input tensor
input_tensor = torch.rand((1, 3, 224, 224))

# Benchmark original model
start_time = time.time()
with torch.no_grad():
    original_output = original_model(input_tensor)
original_time = time.time() - start_time

# Benchmark quantized model
start_time = time.time()
with torch.no_grad():
    quantized_output = quantized_model(input_tensor)
quantized_time = time.time() - start_time

print(f'Original model inference time: {original_time:.4f} seconds')
print(f'Quantized model inference time: {quantized_time:.4f} seconds')
```

> **💡 Tip:** Ensure that the input data for the quantized model is pre-processed correctly, as quantization can be sensitive to input scaling and zero-point values.

Benchmarking is essential to evaluate the performance and efficiency gains of quantized models. It involves comparing the inference speed, memory usage, and accuracy of the quantized model against the original floating-point model to ensure that the quantization process has not adversely affected the model's performance.

```python title="example2.py"
import torch
import time

# Load original and quantized models
original_model = torch.hub.load('pytorch/vision:v0.10.0','mobilenet_v2', pretrained=True)
original_model.eval()
quantized_model = torch.quantization.quantize_dynamic(original_model, {torch.nn.Linear}, dtype=torch.qint8)

# Prepare input tensor
input_tensor = torch.rand((1, 3, 224, 224))

# Benchmark original model
start_time = time.time()
with torch.no_grad():
    original_output = original_model(input_tensor)
original_time = time.time() - start_time

# Benchmark quantized model
start_time = time.time()
with torch.no_grad():
    quantized_output = quantized_model(input_tensor)
quantized_time = time.time() - start_time

print(f'Original model inference time: {original_time:.4f} seconds')
print(f'Quantized model inference time: {quantized_time:.4f} seconds')
```

>
  <p class="font-semibold mb-3">❓ What is the primary goal of Post-Training Quantization?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119488" value="0">
      <span>To increase model accuracy</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119488" value="1">
      <span>To reduce model size and computational requirements</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119488" value="2">
      <span>To improve training speed</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119488" value="3">
      <span>To enhance data privacy</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Benchmarking is essential to evaluate the performance and efficiency gains of quantized models. It involves comparing the inference speed, memory usage, and accuracy of the quantized model against the original floating-point model to ensure that the quantization process has not adversely affected the model's performance.

```python title="example2.py"
import torch
import time

# Load original and quantized models
original_model = torch.hub.load('pytorch/vision:v0.10.0','mobilenet_v2', pretrained=True)
original_model.eval()
quantized_model = torch.quantization.quantize_dynamic(original_model, {torch.nn.Linear}, dtype=torch.qint8)

# Prepare input tensor
input_tensor = torch.rand((1, 3, 224, 224))

# Benchmark original model
start_time = time.time()
with torch.no_grad():
    original_output = original_model(input_tensor)
original_time = time.time() - start_time

# Benchmark quantized model
start_time = time.time()
with torch.no_grad():
    quantized_output = quantized_model(input_tensor)
quantized_time = time.time() - start_time

print(f'Original model inference time: {original_time:.4f} seconds')
print(f'Quantized model inference time: {quantized_time:.4f} seconds')
```

>
  <p class="font-semibold mb-3">❓ Which precision format is commonly used in Post-Training Quantization?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119744" value="0">
      <span>FP32</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119744" value="1">
      <span>FP16</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119744" value="2">
      <span>INT8</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387119744" value="3">
      <span>INT16</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/quantization-engineering/mod-14.ipynb)

