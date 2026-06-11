# SageMaker Pipelines

**Duration:** 15 min

## Overview

SageMaker Pipelines is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding SageMaker Pipelines requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where SageMaker Pipelines connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing SageMaker Pipelines effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply SageMaker Pipelines in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - SageMaker Pipelines behaves differently at scale
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
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.processing import ScriptProcessor
from sagemaker.estimator import Estimator
import sagemaker

session = sagemaker.Session()
role = 'arn:aws:iam::123456789012:role/SageMakerRole'
bucket = session.default_bucket()

# Define processing step
processor = ScriptProcessor(
    role=role,
    instance_type='ml.m5.xlarge',
    instance_count=1,
    framework_version='0.23-1',
    sagemaker_session=session
)

processing_step = ProcessingStep(
    name='ProcessingStep',
    processor=processor,
    code='preprocessing.py',
    inputs=[
        ProcessingInput(
            source=f's3://{bucket}/raw-data/',
            destination='/opt/ml/processing/input'
        )
    ],
    outputs=[
        ProcessingOutput(
            source='/opt/ml/processing/output',
            destination=f's3://{bucket}/processed-data/'
        )
    ]
)

# Define training step
estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=f's3://{bucket}/training-output',
    sagemaker_session=session
)

training_step = TrainingStep(
    name='TrainingStep',
    estimator=estimator,
    inputs={'training': f's3://{bucket}/processed-data/'}
)

# Create pipeline
pipeline = Pipeline(
    name='ml-pipeline',
    parameters=[],
    steps=[processing_step, training_step]
)

# Execute pipeline
pipeline.upsert(role_arn=role)
pipeline.start()
```

```python
from sagemaker.workflow.parameters import ParameterString, ParameterInteger

# Define parameters
instance_type = ParameterString(
    name='InstanceType',
    default_value='ml.m5.xlarge'
)

epochs = ParameterInteger(
    name='Epochs',
    default_value=10
)

# Use parameters in steps
estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type=instance_type,
    output_path=f's3://{bucket}/training-output',
    sagemaker_session=session
)

estimator.set_hyperparameters(epochs=epochs)
```

```python
from sagemaker.workflow.conditions import ConditionGreaterThan
from sagemaker.workflow.steps import ConditionStep

# Create condition
condition = ConditionGreaterThan(
    left=training_step.properties.FinalMetricDataList[0].Value,
    right=0.8
)

# Create conditional step
conditional_step = ConditionStep(
    name='ConditionalDeploymentStep',
    conditions=[condition],
    if_steps=[deployment_step],
    else_steps=[]
)
```

```python
from sagemaker.model_monitor import DataCaptureConfig
from sagemaker.model import Model

# Create model
model = Model(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
    role=role,
    sagemaker_session=session
)

# Register model
from sagemaker.model_registry import ModelPackageGroup

model_package_group = ModelPackageGroup(
    name='xgboost-models',
    model_package_group_description='XGBoost models',
    sagemaker_session=session
)

model_package = model.register(
    model_package_group_name='xgboost-models',
    content_types=['text/csv'],
    response_types=['text/csv'],
    inference_instances=['ml.m5.large'],
    transform_instances=['ml.m5.large']
)
```

```python
# Get pipeline execution details
execution = pipeline.start()
execution_arn = execution.arn

# Check execution status
import boto3

sm_client = boto3.client('sagemaker')
response = sm_client.describe_pipeline_execution(
    PipelineExecutionArn=execution_arn
)

print(f"Status: {response['PipelineExecutionStatus']}")
print(f"Start time: {response['CreationTime']}")
```


## Quiz

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is the primary purpose of SageMaker Pipelines?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="0">
      <span>Orchestrate end-to-end ML workflows</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="1">
      <span>Store training data</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="2">
      <span>Deploy models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374920" value="3">
      <span>Monitor endpoints</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-8.ipynb)

