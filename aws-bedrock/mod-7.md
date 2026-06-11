# Guardrails & Safety

**Duration:** 15 min

## Overview

Guardrails & Safety is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Guardrails & Safety requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Guardrails & Safety connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Guardrails & Safety effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Guardrails & Safety in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Guardrails & Safety behaves differently at scale
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

client = boto3.client('bedrock', region_name='us-east-1')

# Create a guardrail
response = client.create_guardrail(
    name='customer-support-guardrail',
    description='Safety guardrail for customer support chatbot',
    topicPolicyConfig={
        'topicsConfig': [
            {
                'name': 'financial-advice',
                'definition': 'Providing investment or financial advice',
                'examples': [
                    'Should I buy this stock?',
                    'What cryptocurrency should I invest in?'
                ],
                'type': 'DENY'
            },
            {
                'name': 'medical-advice',
                'definition': 'Providing medical or health advice',
                'examples': [
                    'What medicine should I take?',
                    'Is this symptom serious?'
                ],
                'type': 'DENY'
            }
        ]
    },
    contentPolicyConfig={
        'filtersConfig': [
            {
                'type': 'VIOLENCE',
                'inputStrength': 'HIGH',
                'outputStrength': 'HIGH'
            },
            {
                'type': 'HATE',
                'inputStrength': 'HIGH',
                'outputStrength': 'HIGH'
            },
            {
                'type': 'SEXUAL',
                'inputStrength': 'MEDIUM',
                'outputStrength': 'MEDIUM'
            },
            {
                'type': 'INSULTS',
                'inputStrength': 'MEDIUM',
                'outputStrength': 'MEDIUM'
            }
        ]
    },
    sensitiveInformationPolicyConfig={
        'piiEntitiesConfig': [
            {
                'type': 'EMAIL',
                'action': 'ANONYMIZE'
            },
            {
                'type': 'PHONE',
                'action': 'ANONYMIZE'
            },
            {
                'type': 'SSN',
                'action': 'BLOCK'
            },
            {
                'type': 'CREDIT_CARD',
                'action': 'BLOCK'
            }
        ]
    },
    wordPolicyConfig={
        'wordsConfig': [
            {
                'text': 'competitor-name',
                'action': 'BLOCK'
            }
        ],
        'managedWordListConfig': [
            {
                'type': 'PROFANITY'
            }
        ]
    }
)

guardrail_id = response['guardrailId']
print(f"Guardrail ID: {guardrail_id}")
```

```python
# Apply guardrail to model invocation
response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "What is AWS Bedrock?"}
        ]
    }),
    guardrailIdentifier=guardrail_id,
    guardrailVersion='1'
)

result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

```python
# Configure content filters
content_filters = {
    'VIOLENCE': {
        'inputStrength': 'HIGH',      # Filter user input strictly
        'outputStrength': 'HIGH'      # Filter model output strictly
    },
    'HATE': {
        'inputStrength': 'HIGH',
        'outputStrength': 'HIGH'
    },
    'SEXUAL': {
        'inputStrength': 'MEDIUM',    # Medium filtering
        'outputStrength': 'MEDIUM'
    },
    'INSULTS': {
        'inputStrength': 'LOW',       # Light filtering
        'outputStrength': 'MEDIUM'
    },
    'MISCONDUCT': {
        'inputStrength': 'HIGH',
        'outputStrength': 'HIGH'
    }
}

# Strength levels:
# HIGH: Strict filtering, blocks most content
# MEDIUM: Moderate filtering
# LOW: Minimal filtering, only obvious violations
# NONE: No filtering
```

```python
# Configure PII handling
pii_config = {
    'EMAIL': {
        'action': 'ANONYMIZE'  # Replace with [EMAIL]
    },
    'PHONE': {
        'action': 'ANONYMIZE'  # Replace with [PHONE]
    },
    'NAME': {
        'action': 'ANONYMIZE'  # Replace with [NAME]
    },
    'SSN': {
        'action': 'BLOCK'      # Block the entire request
    },
    'CREDIT_CARD': {
        'action': 'BLOCK'      # Block the entire request
    },
    'IP_ADDRESS': {
        'action': 'ANONYMIZE'
    },
    'DRIVER_LICENSE': {
        'action': 'BLOCK'
    }
}

# Example: User input with PII
user_input = "My email is john@example.com and my phone is 555-1234"

# After guardrail processing:
# "My email is [EMAIL] and my phone is [PHONE]"
```

```python
# Define denied topics
denied_topics = [
    {
        'name': 'illegal-activities',
        'definition': 'Instructions for illegal activities',
        'examples': [
            'How to make explosives',
            'How to hack into systems',
            'How to forge documents'
        ],
        'type': 'DENY'
    },
    {
        'name': 'self-harm',
        'definition': 'Content promoting self-harm',
        'examples': [
            'How to hurt myself',
            'Methods of suicide'
        ],
        'type': 'DENY'
    }
]

# Define allowed topics (optional)
allowed_topics = [
    {
        'name': 'product-support',
        'definition': 'Questions about our products',
        'examples': [
            'How do I use feature X?',
            'What are the system requirements?'
        ],
        'type': 'ALLOW'
    }
]
```


## Quiz

---

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the primary purpose of Bedrock Guardrails?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="0">
      <span>To improve model accuracy</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="1">
      <span>To control model behavior and filter harmful content</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="2">
      <span>To reduce API costs</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="3">
      <span>To encrypt model responses</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What does the ANONYMIZE action do for PII?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="0">
      <span>Deletes the PII from the request</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="1">
      <span>Encrypts the PII</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="2">
      <span>Replaces PII with a placeholder like [EMAIL]</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="3">
      <span>Sends PII to a secure vault</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What does a DENY topic policy do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="0">
      <span>Blocks requests related to that topic</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="1">
      <span>Logs requests about that topic</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="2">
      <span>Redirects to a different model</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="3">
      <span>Requires additional authentication</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the difference between HIGH and LOW filter strength?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="0">
      <span>HIGH is faster, LOW is more accurate</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="1">
      <span>HIGH blocks more content strictly, LOW allows more content</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="2">
      <span>HIGH costs more, LOW costs less</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="3">
      <span>They are the same, just different names</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-7.ipynb)

