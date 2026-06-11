# SageMaker Feature Store

**Duration:** 15 min

## Overview

SageMaker Feature Store is a critical component of aws-sagemaker that professionals encounter regularly in production systems.

## Core Concepts

Understanding SageMaker Feature Store requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where SageMaker Feature Store connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing SageMaker Feature Store effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply SageMaker Feature Store in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - SageMaker Feature Store behaves differently at scale
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
from sagemaker.feature_store.feature_group import FeatureGroup
import sagemaker
import pandas as pd

session = sagemaker.Session()
role = 'arn:aws:iam::123456789012:role/SageMakerRole'
bucket = session.default_bucket()

# Create sample data
df = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'age': [25, 30, 35],
    'income': [50000, 60000, 70000],
    'event_time': pd.date_range('2024-01-01', periods=3)
})

# Create feature group
feature_group = FeatureGroup(
    name='customer-features',
    sagemaker_session=session
)

# Load data
feature_group.load_feature_definitions(data_frame=df)

# Create feature group
feature_group.create(
    s3_uri=f's3://{bucket}/feature-store/',
    record_identifier_name='customer_id',
    event_time_feature_name='event_time',
    role_arn=role,
    enable_online_store=True
)

# Ingest data
feature_group.ingest(df, max_workers=3, wait=True)
```

```python
from sagemaker.feature_store.feature_group import FeatureGroup

# Create feature group with both stores
feature_group = FeatureGroup(
    name='transaction-features',
    sagemaker_session=session
)

feature_group.create(
    s3_uri=f's3://{bucket}/feature-store/',
    record_identifier_name='transaction_id',
    event_time_feature_name='timestamp',
    role_arn=role,
    enable_online_store=True,  # For real-time inference
    online_store_kms_key_id=None,
    offline_store_kms_key_id=None
)

# Query online store for inference
import boto3

fs_client = boto3.client('sagemaker-featurestore-runtime')

response = fs_client.get_record(
    FeatureGroupName='transaction-features',
    RecordIdentifierValueAsString='txn-123'
)

print(f"Record: {response['Record']}")
```

```python
import pandas as pd
from sagemaker.feature_store.feature_group import FeatureGroup

# Load data from S3
df = pd.read_csv('s3://my-bucket/raw-features.csv')

# Create feature group
feature_group = FeatureGroup(
    name='product-features',
    sagemaker_session=session
)

# Ingest data
feature_group.ingest(
    data_frame=df,
    max_workers=5,
    wait=True
)

print(f"Ingested {len(df)} records")
```

```python
import boto3
import pandas as pd

athena = boto3.client('athena')

# Query offline store using Athena
query = """
SELECT * FROM "sagemaker_featurestore"."customer_features_1234567890"
WHERE event_time >= '2024-01-01'
LIMIT 100
"""

response = athena.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': 'sagemaker_featurestore'},
    ResultConfiguration={'OutputLocation': f's3://{bucket}/athena-results/'}
)

# Get results
query_id = response['QueryExecutionId']
results = athena.get_query_results(QueryExecutionId=query_id)

df = pd.DataFrame(results['ResultSet']['Rows'])
print(df)
```

```python
from sagemaker.feature_store.feature_group import FeatureGroup
import pandas as pd

# Get feature group
feature_group = FeatureGroup(
    name='customer-features',
    sagemaker_session=session
)

# Query offline store for training data
query = feature_group.athena_query()

query.run(
    query_string=f'SELECT * FROM "{query.table_name}"',
    output_location=f's3://{bucket}/query-results/'
)

# Load results
df = query.as_dataframe()

# Use for training
from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri='382416733822.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=f's3://{bucket}/training-output',
    sagemaker_session=session
)

estimator.fit({'training': f's3://{bucket}/training-data/'})
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-sagemaker/mod-9.ipynb)

