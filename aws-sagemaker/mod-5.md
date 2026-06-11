# Training Jobs

**Duration:** 15 min

## Overview

Training Jobs is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding Training Jobs requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Training Jobs connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Training Jobs effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Training Jobs in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Training Jobs behaves differently at scale
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
from sagemaker.estimator import Estimator
import sagemaker

session = sagemaker.Session()
role = 'arn:aws:iam::123456789012:role/SageMakerRole'
bucket = session.default_bucket()

# Create estimator for custom training script
estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=f's3://{bucket}/training-output',
    code_location=f's3://{bucket}/code',
    sagemaker_session=session
)

# Set hyperparameters
estimator.set_hyperparameters(
    epochs=10,
    batch_size=32,
    learning_rate=0.001,
    optimizer='adam'
)

# Start training
estimator.fit(
    {'training': f's3://{bucket}/train-data/'},
    job_name='training-job-2024-01-15',
    wait=True
)
```

```python
from sagemaker.tensorflow import TensorFlow

# TensorFlow estimator with hyperparameters
tf_estimator = TensorFlow(
    entry_point='train.py',
    role=role,
    instance_count=1,
    instance_type='ml.p3.2xlarge',
    framework_version='2.8',
    py_version='py39',
    output_path=f's3://{bucket}/tf-output',
    sagemaker_session=session,
    hyperparameters={
        'epochs': 50,
        'batch_size': 64,
        'learning_rate': 0.001,
        'dropout': 0.5,
        'activation': 'relu'
    }
)

# Fit the model
tf_estimator.fit(
    {'training': f's3://{bucket}/train-data/'},
    job_name='tensorflow-training'
)
```

```python
from sagemaker.estimator import Estimator

# Enable spot training
estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=f's3://{bucket}/training-output',
    sagemaker_session=session,
    use_spot_instances=True,
    max_run=3600,
    max_wait=5400
)

# Spot training can save up to 90% on compute costs
estimator.fit(
    {'training': f's3://{bucket}/train-data/'},
    job_name='spot-training-job'
)
```

```python
from sagemaker.pytorch import PyTorch

# Distributed training with multiple instances
pytorch_estimator = PyTorch(
    entry_point='train.py',
    role=role,
    instance_count=4,  # Multiple instances
    instance_type='ml.p3.8xlarge',
    framework_version='1.12',
    py_version='py38',
    output_path=f's3://{bucket}/pytorch-output',
    sagemaker_session=session,
    distribution={
        'torch_distributed': {
            'enabled': True
        }
    }
)

# Train with distributed strategy
pytorch_estimator.fit(
    {'training': f's3://{bucket}/train-data/'},
    job_name='distributed-training'
)
```

```python
# Check training job status
import boto3

sm_client = boto3.client('sagemaker')

response = sm_client.describe_training_job(
    TrainingJobName='my-training-job'
)

print(f"Status: {response['TrainingJobStatus']}")
print(f"Start time: {response['CreationTime']}")
print(f"Training time: {response.get('TrainingEndTime', 'In progress')}")
print(f"Billable seconds: {response['BillableTimeInSeconds']}")
```


## Quiz

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the primary purpose of SageMaker Training Jobs?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="0">
      <span>Data storage</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="1">
      <span>Train ML models on managed infrastructure</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="2">
      <span>Real-time predictions</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="3">
      <span>Model monitoring</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-5.ipynb)

