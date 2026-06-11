# Hyperparameter Tuning

**Duration:** 15 min

## Overview

Hyperparameter Tuning is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding Hyperparameter Tuning requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Hyperparameter Tuning connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Hyperparameter Tuning effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Hyperparameter Tuning in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Hyperparameter Tuning behaves differently at scale
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
from sagemaker.tuner import HyperparameterTuner, IntegerParameter, ContinuousParameter, CategoricalParameter
from sagemaker.xgboost import XGBoost
import sagemaker

session = sagemaker.Session()
role = 'arn:aws:iam::123456789012:role/SageMakerRole'
bucket = session.default_bucket()

# Create base estimator
xgb_estimator = XGBoost(
    entry_point='train.py',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    framework_version='1.5',
    output_path=f's3://{bucket}/xgb-output',
    sagemaker_session=session
)

# Define hyperparameter ranges
hyperparameter_ranges = {
    'max_depth': IntegerParameter(1, 10),
    'eta': ContinuousParameter(0.1, 0.5),
    'min_child_weight': IntegerParameter(2, 10),
    'subsample': ContinuousParameter(0.5, 1.0),
    'gamma': ContinuousParameter(0, 5)
}

# Create tuner
tuner = HyperparameterTuner(
    estimator=xgb_estimator,
    objective_metric_name='validation:auc',
    hyperparameter_ranges=hyperparameter_ranges,
    metric_definitions=[
        {'Name': 'validation:auc', 'Regex': 'validation-auc=([0-9\\.]+)'}
    ],
    max_jobs=20,
    max_parallel_jobs=4,
    base_tuning_job_name='xgb-tuning'
)

# Start tuning
tuner.fit(
    {'training': f's3://{bucket}/train-data/'},
    job_name='xgb-tuning-job'
)
```

```python
from sagemaker.tuner import HyperparameterTuner, StrategyConfig

# Configure Bayesian optimization
strategy_config = StrategyConfig(
    strategy='Bayesian',
    metric_definitions=[
        {'Name': 'validation:accuracy', 'Regex': 'accuracy=([0-9\\.]+)'}
    ]
)

tuner = HyperparameterTuner(
    estimator=xgb_estimator,
    objective_metric_name='validation:accuracy',
    hyperparameter_ranges=hyperparameter_ranges,
    max_jobs=30,
    max_parallel_jobs=5,
    strategy='Bayesian'
)

# Bayesian optimization learns from previous trials
tuner.fit({'training': f's3://{bucket}/train-data/'})
```

```python
from sagemaker.tuner import WarmStartConfig, WarmStartTypes

# Use results from previous tuning job
warm_start_config = WarmStartConfig(
    type=WarmStartTypes.TRANSFER_LEARNING,
    from_job_name='xgb-tuning-job-2024-01-10'
)

# Create new tuner with warm start
tuner = HyperparameterTuner(
    estimator=xgb_estimator,
    objective_metric_name='validation:auc',
    hyperparameter_ranges=hyperparameter_ranges,
    max_jobs=20,
    max_parallel_jobs=4,
    warm_start_config=warm_start_config
)

tuner.fit({'training': f's3://{bucket}/train-data/'})
```

```python
# Get best training job
best_job = tuner.best_training_job()
print(f"Best job: {best_job}")

# Get best hyperparameters
best_hyperparameters = tuner.best_estimator().hyperparameters()
print(f"Best hyperparameters: {best_hyperparameters}")

# Deploy best model
best_predictor = tuner.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)
```

```python
from sagemaker.tuner import HyperparameterTuner

tuner = HyperparameterTuner(
    estimator=xgb_estimator,
    objective_metric_name='validation:auc',
    hyperparameter_ranges=hyperparameter_ranges,
    max_jobs=20,
    max_parallel_jobs=4,
    early_stopping_type='Auto'  # Enable automatic early stopping
)

tuner.fit({'training': f's3://{bucket}/train-data/'})
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-6.ipynb)

