# Model Deployment & Endpoints

**Duration:** 15 min

## Overview

Model Deployment & Endpoints is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding Model Deployment & Endpoints requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Model Deployment & Endpoints connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Model Deployment & Endpoints effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Model Deployment & Endpoints in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Model Deployment & Endpoints behaves differently at scale
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

# Train a model
estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path='s3://my-bucket/output',
    sagemaker_session=session
)

estimator.fit({'training': 's3://my-bucket/train-data/'})

# Deploy as real-time endpoint
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    endpoint_name='xgboost-realtime-endpoint'
)

# Make predictions
import csv
import io

test_data = '5.1,3.5,1.4,0.2'
response = predictor.predict(test_data)
print(f"Prediction: {response}")
```

```python
from sagemaker.serverless import ServerlessInferenceConfig

# Create serverless endpoint
serverless_config = ServerlessInferenceConfig(
    memory_size_in_mb=1024,
    max_concurrency=10
)

predictor = estimator.deploy(
    serverless_inference_config=serverless_config,
    endpoint_name='xgboost-serverless-endpoint'
)

# Invoke serverless endpoint
response = predictor.predict(test_data)
print(f"Prediction: {response}")
```

```python
from sagemaker.async_inference.async_inference_config import AsyncInferenceConfig

# Configure async inference
async_config = AsyncInferenceConfig(
    output_path='s3://my-bucket/async-output/',
    max_concurrent_invocations_per_instance=10
)

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    async_inference_config=async_config,
    endpoint_name='xgboost-async-endpoint'
)

# Invoke async endpoint
import json

input_location = 's3://my-bucket/async-input/test-data.json'
response = predictor.predict_async(input_location)
output_location = response.output_location
print(f"Output will be at: {output_location}")
```

```python
from sagemaker.multidatamodel import MultiDataModel

# Create multi-model endpoint
multi_model = MultiDataModel(
    name='multi-model-endpoint',
    model_data_prefix='s3://my-bucket/models/',
    model_name='xgboost-multi',
    container_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    sagemaker_session=session
)

# Add models
multi_model.add('model-1.tar.gz')
multi_model.add('model-2.tar.gz')

# Deploy
predictor = multi_model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)

# Invoke specific model
response = predictor.predict(
    test_data,
    target_model='model-1.tar.gz'
)
```

```python
import boto3

autoscaling = boto3.client('application-autoscaling')

# Register endpoint for auto-scaling
autoscaling.register_scalable_target(
    ServiceNamespace='sagemaker',
    ResourceId='endpoint/my-endpoint/variant/AllTraffic',
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    MinCapacity=1,
    MaxCapacity=10
)

# Create scaling policy
autoscaling.put_scaling_policy(
    PolicyName='endpoint-scaling-policy',
    ServiceNamespace='sagemaker',
    ResourceId='endpoint/my-endpoint/variant/AllTraffic',
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    PolicyType='TargetTrackingScaling',
    TargetTrackingScalingPolicyConfiguration={
        'TargetValue': 70.0,
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'SageMakerVariantInvocationsPerInstance'
        }
    }
)
```


## Quiz

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the primary advantage of real-time endpoints?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="0">
      <span>Low-latency synchronous predictions</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="1">
      <span>Automatic scaling</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="2">
      <span>Batch processing</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="3">
      <span>Cost savings</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-7.ipynb)

