# Monitoring & Cost Optimization

**Duration:** 15 min

## Overview

Monitoring & Cost Optimization is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding Monitoring & Cost Optimization requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Monitoring & Cost Optimization connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Monitoring & Cost Optimization effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Monitoring & Cost Optimization in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Monitoring & Cost Optimization behaves differently at scale
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
from sagemaker.model_monitor import DataQualityMonitor, DataCaptureConfig
import sagemaker

session = sagemaker.Session()
role = 'arn:aws:iam::123456789012:role/SageMakerRole'
bucket = session.default_bucket()

# Enable data capture on endpoint
data_capture_config = DataCaptureConfig(
    enabled=True,
    sampling_percentage=100,
    destination_s3_uri=f's3://{bucket}/data-capture/'
)

# Deploy endpoint with data capture
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    data_capture_config=data_capture_config,
    endpoint_name='monitored-endpoint'
)

# Create baseline
monitor = DataQualityMonitor(
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    sagemaker_session=session
)

# Create baseline from training data
monitor.suggest_baseline(
    baseline_dataset=f's3://{bucket}/train-data/data.csv',
    dataset_format='text/csv'
)

# Schedule monitoring
monitor.create_monitoring_schedule(
    monitor_schedule_name='data-quality-monitor',
    endpoint_input=f's3://{bucket}/data-capture/',
    output_s3_uri=f's3://{bucket}/monitoring-output/',
    statistics=monitor.baseline_statistics(),
    constraints=monitor.baseline_constraints(),
    schedule_expression='cron(0 * * * ? *)'  # Hourly
)
```

```python
import boto3

sm_client = boto3.client('sagemaker')

# Get monitoring execution details
response = sm_client.list_monitoring_executions(
    MonitoringScheduleName='data-quality-monitor'
)

for execution in response['MonitoringExecutionSummaries']:
    print(f"Execution: {execution['MonitoringExecutionArn']}")
    print(f"Status: {execution['MonitoringExecutionStatus']}")
    
    # Get violations
    violations = sm_client.get_monitoring_schedule(
        MonitoringScheduleName='data-quality-monitor'
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
        },
        'ScaleOutCooldown': 300,
        'ScaleInCooldown': 300
    }
)
```

```python
from sagemaker.estimator import Estimator

# Use spot instances for training
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

# Use serverless endpoints for variable traffic
from sagemaker.serverless import ServerlessInferenceConfig

serverless_config = ServerlessInferenceConfig(
    memory_size_in_mb=1024,
    max_concurrency=10
)

predictor = estimator.deploy(
    serverless_inference_config=serverless_config,
    endpoint_name='cost-optimized-endpoint'
)

# Use multi-model endpoints
from sagemaker.multidatamodel import MultiDataModel

multi_model = MultiDataModel(
    name='multi-model-endpoint',
    model_data_prefix=f's3://{bucket}/models/',
    model_name='xgboost-multi',
    container_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    sagemaker_session=session
)

predictor = multi_model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)
```

```python
import boto3

cloudwatch = boto3.client('cloudwatch')

# Get endpoint invocation metrics
response = cloudwatch.get_metric_statistics(
    Namespace='AWS/SageMaker',
    MetricName='InvocationsPerInstance',
    Dimensions=[
        {
            'Name': 'EndpointName',
            'Value': 'my-endpoint'
        },
        {
            'Name': 'VariantName',
            'Value': 'AllTraffic'
        }
    ],
    StartTime='2024-01-01T00:00:00Z',
    EndTime='2024-01-02T00:00:00Z',
    Period=3600,
    Statistics=['Average', 'Sum']
)

print(f"Metrics: {response['Datapoints']}")
```


## Quiz

<div class="quiz">
  <p class="font-semibold mb-3">❓ What does Model Monitor detect?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="0">
      <span>Data drift and model performance degradation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="1">
      <span>Training errors</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="2">
      <span>Deployment failures</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="3">
      <span>Cost overruns</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-10.ipynb)

