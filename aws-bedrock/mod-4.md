# Prompt Engineering for Bedrock

**Duration:** 15 min

## Overview

Prompt Engineering for Bedrock is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Prompt Engineering for Bedrock requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Prompt Engineering for Bedrock connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Prompt Engineering for Bedrock effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Prompt Engineering for Bedrock in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Prompt Engineering for Bedrock behaves differently at scale
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

# Without system prompt
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "What is machine learning?"}
    ]
)

# With system prompt
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "What is machine learning?"}
    ],
    system="You are a beginner-friendly AI tutor. Explain concepts simply with examples."
)

print(response['output']['message']['content'][0]['text'])
```

```python
# Deterministic response (good for Q&A, classification)
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    inferenceConfig={
        "temperature": 0.0,  # Always the same answer
        "maxTokens": 100
    }
)

# Creative response (good for brainstorming, content generation)
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "Write a creative story about AI"}
    ],
    inferenceConfig={
        "temperature": 0.9,  # Varied, creative responses
        "maxTokens": 500
    }
)
```

```python
# Conservative (top_p=0.5): Only consider top 50% of likely tokens
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "Classify this email as spam or not: 'Buy cheap watches now!'"}
    ],
    inferenceConfig={
        "topP": 0.5,
        "temperature": 0.3,
        "maxTokens": 50
    }
)

# Diverse (top_p=0.95): Consider more token options
response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "Generate 3 creative product names for a coffee app"}
    ],
    inferenceConfig={
        "topP": 0.95,
        "temperature": 0.8,
        "maxTokens": 200
    }
)
```

```python
# Stop at newline to get single-line responses
response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 100,
        "stop_sequences": ["\n"],
        "messages": [
            {"role": "user", "content": "List one benefit of AWS Bedrock"}
        ]
    })
)

# Stop at specific marker
response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 500,
        "stop_sequences": ["</answer>"],
        "messages": [
            {"role": "user", "content": "Answer: <answer>What is RAG?</answer>"}
        ]
    })
)
```

```python
prompt = """
Classify the sentiment of these reviews:

Example 1: "This product is amazing!" → Positive
Example 2: "Terrible quality, waste of money" → Negative
Example 3: "It's okay, nothing special" → Neutral

Now classify: "Best purchase I've made all year!"
"""

response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": prompt}
    ],
    inferenceConfig={"maxTokens": 50, "temperature": 0.0}
)
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-4.ipynb)

