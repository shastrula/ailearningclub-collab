# Production Patterns

**Duration:** 15 min

## Overview

Production Patterns is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Production Patterns requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Production Patterns connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Production Patterns effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Production Patterns in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Production Patterns behaves differently at scale
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
import time
from botocore.exceptions import ClientError

client = boto3.client('bedrock-runtime', region_name='us-east-1')

def invoke_with_retry(model_id, body, max_retries=3):
    """Invoke model with exponential backoff retry"""
    
    for attempt in range(max_retries):
        try:
            response = client.invoke_model(
                modelId=model_id,
                body=body
            )
            return response
        
        except ClientError as e:
            error_code = e.response['Error']['Code']
            
            # Retryable errors
            if error_code == 'ThrottlingException':
                wait_time = 2 ** attempt  # Exponential backoff
                print(f'Rate limited. Waiting {wait_time}s...')
                time.sleep(wait_time)
                continue
            
            # Non-retryable errors
            elif error_code == 'AccessDeniedException':
                print('Model access not enabled')
                raise
            elif error_code == 'ValidationException':
                print('Invalid request format')
                raise
            else:
                raise
    
    raise Exception('Max retries exceeded')
```

```python
import json

def estimate_cost(model_id, input_text, output_tokens=100):
    """Estimate API cost before invoking"""
    
    # Pricing per 1K tokens (example rates)
    pricing = {
        'claude-3-sonnet': {'input': 0.003, 'output': 0.015},
        'claude-3-haiku': {'input': 0.00025, 'output': 0.00125},
        'llama3-70b': {'input': 0.00195, 'output': 0.00256},
        'titan-express': {'input': 0.00013, 'output': 0.00017}
    }
    
    # Rough token count (1 token ≈ 4 chars)
    input_tokens = len(input_text) / 4
    
    # Get pricing
    model_key = [k for k in pricing.keys() if k in model_id][0]
    rates = pricing[model_key]
    
    # Calculate cost
    input_cost = (input_tokens / 1000) * rates['input']
    output_cost = (output_tokens / 1000) * rates['output']
    total_cost = input_cost + output_cost
    
    return {
        'input_tokens': int(input_tokens),
        'output_tokens': output_tokens,
        'input_cost': input_cost,
        'output_cost': output_cost,
        'total_cost': total_cost
    }

# Example
cost = estimate_cost(
    'anthropic.claude-3-sonnet-20240229-v1:0',
    'What is AWS Bedrock?',
    output_tokens=100
)
print(f"Estimated cost: ${cost['total_cost']:.6f}")
```

```python
import hashlib
import json
from functools import lru_cache

# In-memory cache
response_cache = {}

def get_cached_response(model_id, prompt, temperature=0.7):
    """Get response from cache or invoke model"""
    
    # Create cache key
    cache_key = hashlib.md5(
        f"{model_id}:{prompt}:{temperature}".encode()
    ).hexdigest()
    
    # Check cache
    if cache_key in response_cache:
        print("Cache hit!")
        return response_cache[cache_key]
    
    # Invoke model
    print("Cache miss. Invoking model...")
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-06-01",
            "max_tokens": 1024,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}]
        })
    )
    
    result = json.loads(response['body'].read())
    
    # Store in cache
    response_cache[cache_key] = result
    
    return result

# Redis cache for distributed systems
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_response_redis(model_id, prompt, ttl=3600):
    """Cache responses in Redis"""
    
    cache_key = hashlib.md5(
        f"{model_id}:{prompt}".encode()
    ).hexdigest()
    
    # Check Redis
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Invoke model
    response = client.invoke_model(...)
    result = json.loads(response['body'].read())
    
    # Store in Redis with TTL
    redis_client.setex(
        cache_key,
        ttl,
        json.dumps(result)
    )
    
    return result
```

```python
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def invoke_with_monitoring(model_id, body):
    """Invoke model with comprehensive monitoring"""
    
    start_time = time.time()
    
    try:
        logger.info(f"Invoking model: {model_id}")
        
        response = client.invoke_model(
            modelId=model_id,
            body=body
        )
        
        result = json.loads(response['body'].read())
        
        # Extract metrics
        duration = time.time() - start_time
        input_tokens = result.get('usage', {}).get('input_tokens', 0)
        output_tokens = result.get('usage', {}).get('output_tokens', 0)
        
        # Log metrics
        logger.info(
            f"Success | Duration: {duration:.2f}s | "
            f"Input: {input_tokens} | Output: {output_tokens}"
        )
        
        # Send to monitoring service (CloudWatch, DataDog, etc.)
        send_metrics({
            'model': model_id,
            'duration': duration,
            'input_tokens': input_tokens,
            'output_tokens': output_tokens,
            'status': 'success'
        })
        
        return result
    
    except Exception as e:
        duration = time.time() - start_time
        logger.error(f"Error: {str(e)} | Duration: {duration:.2f}s")
        
        send_metrics({
            'model': model_id,
            'duration': duration,
            'status': 'error',
            'error': str(e)
        })
        
        raise

def send_metrics(metrics):
    """Send metrics to monitoring service"""
    # Example: CloudWatch
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_data(
        Namespace='BedrockApp',
        MetricData=[
            {
                'MetricName': 'ModelInvocation',
                'Value': metrics['duration'],
                'Unit': 'Seconds',
                'Dimensions': [
                    {'Name': 'Model', 'Value': metrics['model']},
                    {'Name': 'Status', 'Value': metrics['status']}
                ]
            }
        ]
    )
```

```python
import random

def invoke_with_ab_test(prompt, variant_a_model, variant_b_model):
    """A/B test two models"""
    
    # Randomly select variant
    variant = random.choice(['A', 'B'])
    model_id = variant_a_model if variant == 'A' else variant_b_model
    
    # Invoke model
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-06-01",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        })
    )
    
    result = json.loads(response['body'].read())
    
    # Log for analysis
    logger.info(f"A/B Test | Variant: {variant} | Model: {model_id}")
    
    # Store result with variant for later analysis
    store_ab_result({
        'variant': variant,
        'model': model_id,
        'response': result,
        'timestamp': datetime.now().isoformat()
    })
    
    return result

def analyze_ab_test_results():
    """Analyze A/B test results"""
    # Query stored results
    # Calculate metrics: latency, cost, user satisfaction
    # Determine winner
    pass
```


## Quiz

**AWS Bedrock Documentation:**
- https://docs.aws.amazon.com/bedrock/
- https://docs.aws.amazon.com/bedrock/latest/userguide/

**Model Documentation:**
- Claude: https://docs.anthropic.com/claude/reference/
- Llama: https://www.llama.com/docs/
- Mistral: https://docs.mistral.ai/
- Stable Diffusion: https://huggingface.co/stabilityai

**LangChain:**
- https://python.langchain.com/docs/
- https://python.langchain.com/docs/integrations/providers/bedrock

**Best Practices:**
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- Prompt Engineering Guide: https://www.promptingguide.ai/
- RAG Best Practices: https://aws.amazon.com/blogs/machine-learning/

**Community:**
- AWS Bedrock Discord: https://discord.gg/bedrock
- Stack Overflow: Tag `aws-bedrock`
- GitHub: https://github.com/aws/bedrock-examples

---

**AWS Bedrock Documentation:**
- https://docs.aws.amazon.com/bedrock/
- https://docs.aws.amazon.com/bedrock/latest/userguide/

**Model Documentation:**
- Claude: https://docs.anthropic.com/claude/reference/
- Llama: https://www.llama.com/docs/
- Mistral: https://docs.mistral.ai/
- Stable Diffusion: https://huggingface.co/stabilityai

**LangChain:**
- https://python.langchain.com/docs/
- https://python.langchain.com/docs/integrations/providers/bedrock

**Best Practices:**
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- Prompt Engineering Guide: https://www.promptingguide.ai/
- RAG Best Practices: https://aws.amazon.com/blogs/machine-learning/

**Community:**
- AWS Bedrock Discord: https://discord.gg/bedrock
- Stack Overflow: Tag `aws-bedrock`
- GitHub: https://github.com/aws/bedrock-examples

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is exponential backoff used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="0">
      <span>Reducing API costs</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="1">
      <span>Handling rate limiting by increasing wait time between retries</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="2">
      <span>Improving model accuracy</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="3">
      <span>Filtering harmful content</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

**AWS Bedrock Documentation:**
- https://docs.aws.amazon.com/bedrock/
- https://docs.aws.amazon.com/bedrock/latest/userguide/

**Model Documentation:**
- Claude: https://docs.anthropic.com/claude/reference/
- Llama: https://www.llama.com/docs/
- Mistral: https://docs.mistral.ai/
- Stable Diffusion: https://huggingface.co/stabilityai

**LangChain:**
- https://python.langchain.com/docs/
- https://python.langchain.com/docs/integrations/providers/bedrock

**Best Practices:**
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- Prompt Engineering Guide: https://www.promptingguide.ai/
- RAG Best Practices: https://aws.amazon.com/blogs/machine-learning/

**Community:**
- AWS Bedrock Discord: https://discord.gg/bedrock
- Stack Overflow: Tag `aws-bedrock`
- GitHub: https://github.com/aws/bedrock-examples

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the main benefit of caching responses?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="0">
      <span>Improved model accuracy</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="1">
      <span>Reduced latency for repeated queries</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="2">
      <span>Reduced latency and cost for repeated queries</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="3">
      <span>Better security</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

**AWS Bedrock Documentation:**
- https://docs.aws.amazon.com/bedrock/
- https://docs.aws.amazon.com/bedrock/latest/userguide/

**Model Documentation:**
- Claude: https://docs.anthropic.com/claude/reference/
- Llama: https://www.llama.com/docs/
- Mistral: https://docs.mistral.ai/
- Stable Diffusion: https://huggingface.co/stabilityai

**LangChain:**
- https://python.langchain.com/docs/
- https://python.langchain.com/docs/integrations/providers/bedrock

**Best Practices:**
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- Prompt Engineering Guide: https://www.promptingguide.ai/
- RAG Best Practices: https://aws.amazon.com/blogs/machine-learning/

**Community:**
- AWS Bedrock Discord: https://discord.gg/bedrock
- Stack Overflow: Tag `aws-bedrock`
- GitHub: https://github.com/aws/bedrock-examples

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is A/B testing used for in production?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="0">
      <span>Comparing two model variants to determine which performs better</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="1">
      <span>Reducing API costs</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="2">
      <span>Filtering harmful content</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="3">
      <span>Improving model accuracy</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

**AWS Bedrock Documentation:**
- https://docs.aws.amazon.com/bedrock/
- https://docs.aws.amazon.com/bedrock/latest/userguide/

**Model Documentation:**
- Claude: https://docs.anthropic.com/claude/reference/
- Llama: https://www.llama.com/docs/
- Mistral: https://docs.mistral.ai/
- Stable Diffusion: https://huggingface.co/stabilityai

**LangChain:**
- https://python.langchain.com/docs/
- https://python.langchain.com/docs/integrations/providers/bedrock

**Best Practices:**
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/
- Prompt Engineering Guide: https://www.promptingguide.ai/
- RAG Best Practices: https://aws.amazon.com/blogs/machine-learning/

**Community:**
- AWS Bedrock Discord: https://discord.gg/bedrock
- Stack Overflow: Tag `aws-bedrock`
- GitHub: https://github.com/aws/bedrock-examples

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What should you do before invoking a model in production?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="0">
      <span>Nothing, just invoke it</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="1">
      <span>Validate the request and estimate costs</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="2">
      <span>Always use the most expensive model</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="3">
      <span>Cache all responses indefinitely</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-10.ipynb)

