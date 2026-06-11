# Bedrock API & boto3

**Duration:** 15 min

## Overview

Bedrock API & boto3 is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Bedrock API & boto3 requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Bedrock API & boto3 connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Bedrock API & boto3 effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Bedrock API & boto3 in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Bedrock API & boto3 behaves differently at scale
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

client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Invoke Claude 3 Sonnet
response = client.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "What is machine learning?"
            }
        ]
    })
)

# Parse response
result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

```python
# Claude format
claude_body = {
    "anthropic_version": "bedrock-2023-06-01",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello"}]
}

# Llama format
llama_body = {
    "prompt": "What is AI?",
    "max_gen_len": 512,
    "temperature": 0.7,
    "top_p": 0.9
}

# Mistral format
mistral_body = {
    "prompt": "Explain quantum computing",
    "max_tokens": 512,
    "temperature": 0.7
}

# Titan format
titan_body = {
    "inputText": "Summarize AWS",
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "temperature": 0.7,
        "topP": 0.9
    }
}
```

```python
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Start a conversation
messages = [
    {
        "role": "user",
        "content": "What is AWS Bedrock?"
    }
]

response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=messages,
    system="You are a helpful AWS expert.",
    inferenceConfig={
        "maxTokens": 1024,
        "temperature": 0.7
    }
)

assistant_message = response['output']['message']['content'][0]['text']
print(assistant_message)

# Continue conversation
messages.append({
    "role": "assistant",
    "content": assistant_message
})

messages.append({
    "role": "user",
    "content": "How does it compare to OpenAI?"
})

response = client.converse(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=messages,
    system="You are a helpful AWS expert.",
    inferenceConfig={
        "maxTokens": 1024,
        "temperature": 0.7
    }
)

print(response['output']['message']['content'][0]['text'])
```

```python
# Streaming with InvokeModel
response = client.invoke_model_with_response_stream(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-06-01",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Write a 500-word essay on AI"}
        ]
    })
)

# Process stream
for event in response['body']:
    if 'contentBlockDelta' in event:
        delta = event['contentBlockDelta']['delta']
        if 'text' in delta:
            print(delta['text'], end='', flush=True)

print()  # Newline after streaming completes
```

```python
# Streaming with Converse
response = client.converse_stream(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=[
        {"role": "user", "content": "Explain quantum computing in detail"}
    ],
    inferenceConfig={
        "maxTokens": 2048,
        "temperature": 0.7
    }
)

# Process stream
for event in response['stream']:
    if 'contentBlockDelta' in event:
        print(event['contentBlockDelta']['delta']['text'], end='', flush=True)
```


## Quiz

```json
{
  "claude_response": {
    "content": [
      {
        "type": "text",
        "text": "Response text here"
      }
    ],
    "usage": {
      "input_tokens": 10,
      "output_tokens": 50
    },
    "stop_reason": "end_turn"
  },
  "llama_response": {
    "generation": "Response text here",
    "prompt_token_count": 10,
    "generation_token_count": 50,
    "stop_reason": "length"
  },
  "converse_response": {
    "output": {
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Response text here"
          }
        ]
      }
    },
    "usage": {
      "inputTokens": 10,
      "outputTokens": 50
    },
    "stopReason": "end_turn"
  }
}
```

---

```json
{
  "claude_response": {
    "content": [
      {
        "type": "text",
        "text": "Response text here"
      }
    ],
    "usage": {
      "input_tokens": 10,
      "output_tokens": 50
    },
    "stop_reason": "end_turn"
  },
  "llama_response": {
    "generation": "Response text here",
    "prompt_token_count": 10,
    "generation_token_count": 50,
    "stop_reason": "length"
  },
  "converse_response": {
    "output": {
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Response text here"
          }
        ]
      }
    },
    "usage": {
      "inputTokens": 10,
      "outputTokens": 50
    },
    "stopReason": "end_turn"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the main advantage of the Converse API over InvokeModel?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7382946" value="0">
      <span>It's faster</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7382946" value="1">
      <span>It handles message formatting automatically for multi-turn conversations</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7382946" value="2">
      <span>It supports more models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7382946" value="3">
      <span>It's cheaper</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude_response": {
    "content": [
      {
        "type": "text",
        "text": "Response text here"
      }
    ],
    "usage": {
      "input_tokens": 10,
      "output_tokens": 50
    },
    "stop_reason": "end_turn"
  },
  "llama_response": {
    "generation": "Response text here",
    "prompt_token_count": 10,
    "generation_token_count": 50,
    "stop_reason": "length"
  },
  "converse_response": {
    "output": {
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Response text here"
          }
        ]
      }
    },
    "usage": {
      "inputTokens": 10,
      "outputTokens": 50
    },
    "stopReason": "end_turn"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ Which method should you use for long-running responses to improve user experience?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="0">
      <span>InvokeModel with polling</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="1">
      <span>Converse API</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="2">
      <span>Streaming with invoke_model_with_response_stream or converse_stream</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="3">
      <span>Multiple sequential InvokeModel calls</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude_response": {
    "content": [
      {
        "type": "text",
        "text": "Response text here"
      }
    ],
    "usage": {
      "input_tokens": 10,
      "output_tokens": 50
    },
    "stop_reason": "end_turn"
  },
  "llama_response": {
    "generation": "Response text here",
    "prompt_token_count": 10,
    "generation_token_count": 50,
    "stop_reason": "length"
  },
  "converse_response": {
    "output": {
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Response text here"
          }
        ]
      }
    },
    "usage": {
      "inputTokens": 10,
      "outputTokens": 50
    },
    "stopReason": "end_turn"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What error indicates that a model hasn't been enabled in your AWS account?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="0">
      <span>AccessDeniedException</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="1">
      <span>ThrottlingException</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="2">
      <span>ValidationException</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="3">
      <span>ModelNotFoundException</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

```json
{
  "claude_response": {
    "content": [
      {
        "type": "text",
        "text": "Response text here"
      }
    ],
    "usage": {
      "input_tokens": 10,
      "output_tokens": 50
    },
    "stop_reason": "end_turn"
  },
  "llama_response": {
    "generation": "Response text here",
    "prompt_token_count": 10,
    "generation_token_count": 50,
    "stop_reason": "length"
  },
  "converse_response": {
    "output": {
      "message": {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "Response text here"
          }
        ]
      }
    },
    "usage": {
      "inputTokens": 10,
      "outputTokens": 50
    },
    "stopReason": "end_turn"
  }
}
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ How can you estimate the cost of an API call before invoking?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="0">
      <span>Use the AWS pricing calculator</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="1">
      <span>Count tokens in the response's usage field</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="2">
      <span>Call the GetTokenCount API</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="3">
      <span>Tokens cannot be counted in advance</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-3.ipynb)

