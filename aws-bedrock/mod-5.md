# Knowledge Bases & RAG

**Duration:** 15 min

## Overview

Knowledge Bases & RAG is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Knowledge Bases & RAG requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Knowledge Bases & RAG connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Knowledge Bases & RAG effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Knowledge Bases & RAG in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Knowledge Bases & RAG behaves differently at scale
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

client = boto3.client('bedrock-agent', region_name='us-east-1')

# Create a knowledge base
response = client.create_knowledge_base(
    name='company-docs-kb',
    description='Company policies and procedures',
    roleArn='arn:aws:iam::ACCOUNT:role/BedrockKBRole',
    knowledgeBaseConfiguration={
        'type': 'VECTOR',
        'vectorKnowledgeBaseConfiguration': {
            'embeddingModel': {
                'provider': 'BEDROCK',
                'modelIdentifier': 'amazon.titan-embed-text-v2:0'
            }
        }
    },
    storageConfiguration={
        'type': 'OPENSEARCH_SERVERLESS',
        'opensearchServerlessConfiguration': {
            'collectionArn': 'arn:aws:aoss:us-east-1:ACCOUNT:collection/...'
        }
    }
)

kb_id = response['knowledgeBase']['id']
print(f"Knowledge Base ID: {kb_id}")
```

```python
# Create a data source
response = client.create_data_source(
    knowledgeBaseId=kb_id,
    name='s3-policies',
    description='Company policies from S3',
    dataSourceConfiguration={
        'type': 'S3',
        's3Configuration': {
            'bucketArn': 'arn:aws:s3:::my-company-docs',
            'inclusionPrefixes': ['policies/'],
            'documentEncodingConfiguration': {
                'encoding': 'UTF-8'
            }
        }
    }
)

data_source_id = response['dataSource']['id']

# Ingest documents
response = client.start_ingestion_job(
    knowledgeBaseId=kb_id,
    dataSourceId=data_source_id
)

print(f"Ingestion Job: {response['ingestionJob']['ingestionJobId']}")
```

```python
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Generate embeddings for text
response = bedrock.invoke_model(
    modelId='amazon.titan-embed-text-v2:0',
    body=json.dumps({
        "inputText": "AWS Bedrock is a managed service for foundation models"
    })
)

result = json.loads(response['body'].read())
embedding = result['embedding']  # List of 1024 floats

print(f"Embedding dimension: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
```

```python
def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks"""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

# Example
document = """
AWS Bedrock is a fully managed service that provides access to foundation models.
It supports multiple models from different providers including Anthropic, Meta, Mistral, and Stability AI.
Bedrock handles scaling, availability, and security automatically.
You can use Bedrock for various tasks including content generation, code assistance, and RAG.
"""

chunks = chunk_text(document, chunk_size=200, overlap=50)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk[:50]}...")
```

```python
from boto3 import client as boto3_client

bedrock_agent_runtime = boto3_client('bedrock-agent-runtime', region_name='us-east-1')

# Retrieve documents from knowledge base
response = bedrock_agent_runtime.retrieve(
    knowledgeBaseId=kb_id,
    retrievalQuery={
        'text': 'What is the vacation policy?'
    },
    retrievalConfiguration={
        'vectorSearchConfiguration': {
            'numberOfResults': 5,
            'overrideSearchType': 'SEMANTIC'
        }
    }
)

# Process results
for result in response['retrievalResults']:
    print(f"Score: {result['score']}")
    print(f"Content: {result['content']['text'][:200]}...")
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-5.ipynb)

