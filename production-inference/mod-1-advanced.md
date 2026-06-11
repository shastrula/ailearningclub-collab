# Production Inference: vLLM, TensorRT-LLM & Quantization

**Duration:** 15 min

## Overview

Production Inference: vLLM, TensorRT-LLM & Quantization is a critical component of production-inference that professionals encounter regularly in production systems.

## Core Concepts

Understanding Production Inference: vLLM, TensorRT-LLM & Quantization requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Production Inference: vLLM, TensorRT-LLM & Quantization connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Production Inference: vLLM, TensorRT-LLM & Quantization effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Production Inference: vLLM, TensorRT-LLM & Quantization in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Production Inference: vLLM, TensorRT-LLM & Quantization behaves differently at scale
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
from vllm import LLM, SamplingParams

# Initialize vLLM with paged attention
llm = LLM(
    model="meta-llama/Llama-2-70b-hf",
    tensor_parallel_size=8,  # Distribute across 8 GPUs
    gpu_memory_utilization=0.9,  # Use 90% of GPU memory
    enable_prefix_caching=True,  # Cache repeated prefixes
)

# Batch inference (vLLM handles scheduling)
prompts = [
    "What is machine learning?",
    "Explain deep learning",
    "Define neural networks",
] * 100  # 300 prompts

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=256,
)

# vLLM automatically batches and schedules
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```

```python
import time
import torch

# Standard inference (naive batching)
def standard_inference(model, prompts, batch_size=1):
    outputs = []
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i+batch_size]
        with torch.no_grad():
            output = model.generate(batch, max_length=256)
        outputs.extend(output)
    return outputs

# vLLM inference
def vllm_inference(llm, prompts):
    return llm.generate(prompts, SamplingParams(max_tokens=256))

# Benchmark
prompts = ["What is AI?"] * 1000

start = time.time()
standard_inference(model, prompts, batch_size=32)
standard_time = time.time() - start

start = time.time()
vllm_inference(llm, prompts)
vllm_time = time.time() - start

print(f"Standard: {standard_time:.2f}s")
print(f"vLLM: {vllm_time:.2f}s")
print(f"Speedup: {standard_time / vllm_time:.1f}x")
```

```python
from tensorrt_llm.runtime import ModelRunner

# Load compiled model
runner = ModelRunner.from_dir(
    engine_dir="./llama-2-70b-trt",
    rank=0,  # GPU rank
    debug_mode=False,
)

# Prepare input
input_ids = tokenizer.encode("What is AI?")
input_ids = torch.tensor([input_ids]).cuda()

# Generate
output_ids = runner.generate(
    input_ids,
    max_new_tokens=256,
    temperature=0.7,
)

output_text = tokenizer.decode(output_ids[0])
print(output_text)
```

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

# 8-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=6.0,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b-hf",
    quantization_config=quantization_config,
    device_map="auto",
)

# Model is now 70B → 17.5B (4x smaller)
print(f"Model size: {model.get_memory_footprint() / 1e9:.1f} GB")
```

```python
# Llama 2 70B inference costs

# Standard (FP16)
cost_standard = 280 * 0.0001  # $0.028 per GB-hour
print(f"Standard: ${cost_standard:.3f}/hour")

# INT8 quantized
cost_int8 = 70 * 0.0001
print(f"INT8: ${cost_int8:.3f}/hour")

# GGUF on local GPU
cost_local = 0.01  # Electricity only
print(f"Local GGUF: ${cost_local:.3f}/hour")

print(f"Savings: {cost_standard / cost_int8:.1f}x cheaper with INT8")
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/production-inference/mod-1-advanced.ipynb)

