# Fine-tuning & Custom Models

**Duration:** 15 min

## Overview

Fine-tuning & Custom Models is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Fine-tuning & Custom Models requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Fine-tuning & Custom Models connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Fine-tuning & Custom Models effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Fine-tuning & Custom Models in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Fine-tuning & Custom Models behaves differently at scale
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
# ✅ Good candidates for fine-tuning:
# - Specialized domain (medical, legal, finance)
# - Specific writing style or tone
# - Consistent output format
# - Limited training data (100+ examples)

# ❌ Not good candidates:
# - General-purpose tasks (use prompt engineering)
# - Very small datasets (<50 examples)
# - Rapidly changing requirements
```

```python
import json

# Training data format for Claude fine-tuning
training_data = [
    {
        "messages": [
            {
                "role": "user",
                "content": "Classify this email: 'Buy cheap watches now!'"
            },
            {
                "role": "assistant",
                "content": "This is spam. It uses urgency and promotional language."
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Classify this email: 'Your meeting is scheduled for 2 PM'"
            },
            {
                "role": "assistant",
                "content": "This is legitimate. It's a calendar notification."
            }
        ]
    }
]

# Save to JSONL format (one JSON object per line)
with open('training_data.jsonl', 'w') as f:
    for example in training_data:
        f.write(json.dumps(example) + '\n')

# Upload to S3
import boto3
s3 = boto3.client('s3')
s3.upload_file('training_data.jsonl', 'my-bucket', 'training/data.jsonl')
```

```python
import boto3

client = boto3.client('bedrock', region_name='us-east-1')

# Create a fine-tuning job
response = client.create_model_customization_job(
    jobName='email-classifier-ft',
    customModelName='email-classifier-v1',
    roleArn='arn:aws:iam::ACCOUNT:role/BedrockFineTuningRole',
    baseModelIdentifier='anthropic.claude-3-sonnet-20240229-v1:0',
    trainingDataConfig={
        's3Uri': 's3://my-bucket/training/data.jsonl'
    },
    outputDataConfig={
        's3OutputPath': 's3://my-bucket/output/'
    },
    hyperParameters={
        'epochs': '3',
        'batchSize': '8',
        'learningRate': '0.0001'
    }
)

job_id = response['jobArn']
print(f"Fine-tuning job started: {job_id}")
```

```python
# Check job status
response = client.get_model_customization_job(
    jobIdentifier=job_id
)

status = response['status']
print(f"Status: {status}")

if status == 'Completed':
    model_arn = response['outputModelArn']
    print(f"Custom model ARN: {model_arn}")
elif status == 'Failed':
    print(f"Error: {response['failureMessage']}")
```

```python
# Invoke the fine-tuned model
response = client.invoke_model(
    modelId='arn:aws:bedrock:us-east-1:ACCOUNT:custom-model/email-classifier-v1',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 100,
        "messages": [
            {
                "role": "user",
                "content": "Classify: 'Limited time offer - 50% off today!'"
            }
        ]
    })
)

result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-8.ipynb)

