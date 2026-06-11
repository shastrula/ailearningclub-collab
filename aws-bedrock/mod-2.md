# Available Models & Selection

**Duration:** 15 min

## Overview

Available Models & Selection is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Available Models & Selection requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Available Models & Selection connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Available Models & Selection effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Available Models & Selection in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Available Models & Selection behaves differently at scale
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
import boto3
import json

client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Using Claude 3 Sonnet
response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Explain quantum computing"}
        ]
    })
)

print(json.loads(response['body'].read())['content'][0]['text'])
```

```python
# Using Llama 3 70B
response = client.invoke_model(
    modelId='meta.llama3-70b-instruct-v1:0',
    body=json.dumps({
        "prompt": "What is machine learning?",
        "max_gen_len": 512,
        "temperature": 0.7,
        "top_p": 0.9
    })
)

result = json.loads(response['body'].read())
print(result['generation'])
```

```python
# Using Mistral Large
response = client.invoke_model(
    modelId='mistral.mistral-large-2402-v1:0',
    body=json.dumps({
        "prompt": "Explain RAG systems",
        "max_tokens": 512,
        "temperature": 0.7
    })
)

result = json.loads(response['body'].read())
print(result['outputs'][0]['text'])
```

```python
# Using Titan Text Express
response = client.invoke_model(
    modelId='amazon.titan-text-express-v1:0',
    body=json.dumps({
        "inputText": "Summarize AWS Bedrock",
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0.7,
            "topP": 0.9
        }
    })
)

result = json.loads(response['body'].read())
print(result['results'][0]['outputText'])
```

```python
import base64

# Generate an image
response = client.invoke_model(
    modelId='stability.stable-diffusion-xl-v1:0',
    body=json.dumps({
        "text_prompts": [
            {"text": "A futuristic AI assistant", "weight": 1.0}
        ],
        "cfg_scale": 10,
        "steps": 50,
        "seed": 0
    })
)

result = json.loads(response['body'].read())
image_data = base64.b64decode(result['artifacts'][0]['base64'])
with open('generated_image.png', 'wb') as f:
    f.write(image_data)
```


## Quiz

```json
{
  "claude": {
    "opus": "anthropic.claude-3-opus-20240229-v1:0",
    "sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "haiku": "anthropic.claude-3-haiku-20240307-v1:0"
  },
  "llama": {
    "llama3_70b": "meta.llama3-70b-instruct-v1:0",
    "llama3_8b": "meta.llama3-8b-instruct-v1:0",
    "llama2_70b": "meta.llama2-70b-chat-v1:0"
  },
  "mistral": {
    "large": "mistral.mistral-large-2402-v1:0",
    "7b": "mistral.mistral-7b-instruct-v0:2"
  },
  "titan": {
    "text_premier": "amazon.titan-text-premier-v1:0",
    "text_express": "amazon.titan-text-express-v1:0",
    "embeddings": "amazon.titan-embed-text-v2:0"
  }
}
```

---

```json
{
  "claude": {
    "opus": "anthropic.claude-3-opus-20240229-v1:0",
    "sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "haiku": "anthropic.claude-3-haiku-20240307-v1:0"
  },
  "llama": {
    "llama3_70b": "meta.llama3-70b-instruct-v1:0",
    "llama3_8b": "meta.llama3-8b-instruct-v1:0",
    "llama2_70b": "meta.llama2-70b-chat-v1:0"
  },
  "mistral": {
    "large": "mistral.mistral-large-2402-v1:0",
    "7b": "mistral.mistral-7b-instruct-v0:2"
  },
  "titan": {
    "text_premier": "amazon.titan-text-premier-v1:0",
    "text_express": "amazon.titan-text-express-v1:0",
    "embeddings": "amazon.titan-embed-text-v2:0"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ Which Claude 3 model offers the best balance of speed and capability?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="0">
      <span>Claude 3 Opus</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="1">
      <span>Claude 3 Sonnet</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="2">
      <span>Claude 3 Haiku</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="3">
      <span>All are equally balanced</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude": {
    "opus": "anthropic.claude-3-opus-20240229-v1:0",
    "sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "haiku": "anthropic.claude-3-haiku-20240307-v1:0"
  },
  "llama": {
    "llama3_70b": "meta.llama3-70b-instruct-v1:0",
    "llama3_8b": "meta.llama3-8b-instruct-v1:0",
    "llama2_70b": "meta.llama2-70b-chat-v1:0"
  },
  "mistral": {
    "large": "mistral.mistral-large-2402-v1:0",
    "7b": "mistral.mistral-7b-instruct-v0:2"
  },
  "titan": {
    "text_premier": "amazon.titan-text-premier-v1:0",
    "text_express": "amazon.titan-text-express-v1:0",
    "embeddings": "amazon.titan-embed-text-v2:0"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ Which model family is best for cost-sensitive, high-volume tasks?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6291847" value="0">
      <span>Claude 3 Opus</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6291847" value="1">
      <span>Mistral Large</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6291847" value="2">
      <span>Llama 3 8B or Mistral 7B</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6291847" value="3">
      <span>Stable Diffusion 3</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude": {
    "opus": "anthropic.claude-3-opus-20240229-v1:0",
    "sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "haiku": "anthropic.claude-3-haiku-20240307-v1:0"
  },
  "llama": {
    "llama3_70b": "meta.llama3-70b-instruct-v1:0",
    "llama3_8b": "meta.llama3-8b-instruct-v1:0",
    "llama2_70b": "meta.llama2-70b-chat-v1:0"
  },
  "mistral": {
    "large": "mistral.mistral-large-2402-v1:0",
    "7b": "mistral.mistral-7b-instruct-v0:2"
  },
  "titan": {
    "text_premier": "amazon.titan-text-premier-v1:0",
    "text_express": "amazon.titan-text-express-v1:0",
    "embeddings": "amazon.titan-embed-text-v2:0"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is Titan Embeddings used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7465382" value="0">
      <span>Generating vector embeddings for RAG systems</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7465382" value="1">
      <span>Image generation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7465382" value="2">
      <span>Code generation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7465382" value="3">
      <span>Fine-tuning other models</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude": {
    "opus": "anthropic.claude-3-opus-20240229-v1:0",
    "sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "haiku": "anthropic.claude-3-haiku-20240307-v1:0"
  },
  "llama": {
    "llama3_70b": "meta.llama3-70b-instruct-v1:0",
    "llama3_8b": "meta.llama3-8b-instruct-v1:0",
    "llama2_70b": "meta.llama2-70b-chat-v1:0"
  },
  "mistral": {
    "large": "mistral.mistral-large-2402-v1:0",
    "7b": "mistral.mistral-7b-instruct-v0:2"
  },
  "titan": {
    "text_premier": "amazon.titan-text-premier-v1:0",
    "text_express": "amazon.titan-text-express-v1:0",
    "embeddings": "amazon.titan-embed-text-v2:0"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ Which model would you choose for complex multi-step reasoning?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="0">
      <span>Llama 3 8B</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="1">
      <span>Mistral 7B</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="2">
      <span>Claude 3 Haiku</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="3">
      <span>Claude 3 Opus</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-2.ipynb)

