# Agents for Bedrock

**Duration:** 15 min

## Overview

Agents for Bedrock is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Agents for Bedrock requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Agents for Bedrock connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Agents for Bedrock effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Agents for Bedrock in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Agents for Bedrock behaves differently at scale
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

# Create an agent
response = client.create_agent(
    agentName='customer-support-agent',
    agentRoleArn='arn:aws:iam::ACCOUNT:role/BedrockAgentRole',
    description='Handles customer support queries',
    foundationModel='anthropic.claude-3-sonnet-20240229-v1:0',
    instruction="""You are a helpful customer support agent. 
    Use available tools to help customers with their issues.
    Always be polite and try to resolve issues quickly."""
)

agent_id = response['agent']['id']
print(f"Agent ID: {agent_id}")
```

```python
# Define an action group
action_group_config = {
    'actionGroupName': 'customer-tools',
    'description': 'Tools for customer support',
    'actionGroupExecutor': {
        'lambda': 'arn:aws:lambda:us-east-1:ACCOUNT:function:customer-support-handler'
    },
    'apiSchema': {
        'payload': json.dumps({
            "openapi": "3.0.0",
            "info": {"title": "Customer Support API", "version": "1.0"},
            "paths": {
                "/get-order": {
                    "post": {
                        "summary": "Get order details",
                        "parameters": [
                            {
                                "name": "order_id",
                                "in": "query",
                                "required": True,
                                "schema": {"type": "string"}
                            }
                        ]
                    }
                },
                "/refund": {
                    "post": {
                        "summary": "Process a refund",
                        "parameters": [
                            {
                                "name": "order_id",
                                "in": "query",
                                "required": True,
                                "schema": {"type": "string"}
                            },
                            {
                                "name": "reason",
                                "in": "query",
                                "required": True,
                                "schema": {"type": "string"}
                            }
                        ]
                    }
                }
            }
        })
    }
}

# Add action group to agent
response = client.create_agent_action_group(
    agentId=agent_id,
    agentVersion='DRAFT',
    actionGroupName=action_group_config['actionGroupName'],
    description=action_group_config['description'],
    actionGroupExecutor=action_group_config['actionGroupExecutor'],
    apiSchema=action_group_config['apiSchema']
)
```

```python
# Lambda function to handle agent actions
import json
import boto3

def lambda_handler(event, context):
    """Handle agent action calls"""
    
    # Parse the action request
    action_group = event['actionGroup']
    api_path = event['apiPath']
    http_method = event['httpMethod']
    parameters = event.get('parameters', [])
    
    # Extract parameters
    params = {}
    for param in parameters:
        params[param['name']] = param['value']
    
    # Route to appropriate handler
    if api_path == '/get-order':
        return get_order(params['order_id'])
    elif api_path == '/refund':
        return process_refund(params['order_id'], params['reason'])
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Unknown action'})
        }

def get_order(order_id):
    """Fetch order details from database"""
    # In real scenario, query database
    return {
        'statusCode': 200,
        'body': json.dumps({
            'order_id': order_id,
            'status': 'shipped',
            'total': 99.99,
            'items': ['Item 1', 'Item 2']
        })
    }

def process_refund(order_id, reason):
    """Process refund for an order"""
    # In real scenario, update database and payment system
    return {
        'statusCode': 200,
        'body': json.dumps({
            'success': True,
            'refund_id': f'REF-{order_id}',
            'amount': 99.99,
            'message': f'Refund processed for reason: {reason}'
        })
    }
```

```python
# Invoke the agent
response = client.invoke_agent(
    agentId=agent_id,
    agentAliasId='LFTSTCQMTR',  # Use DRAFT for testing
    sessionId='session-123',
    inputText='I want to return my order #12345'
)

# Process streaming response
for event in response['completion']:
    if 'chunk' in event:
        chunk = event['chunk']
        if 'bytes' in chunk:
            print(chunk['bytes'].decode('utf-8'), end='', flush=True)
```

```python
# Multi-step agent workflow
def orchestrate_support_request(customer_id, issue_type):
    """Orchestrate a complex support request"""
    
    agent_client = boto3.client('bedrock-agent-runtime', region_name='us-east-1')
    
    # Step 1: Retrieve customer info
    response = agent_client.invoke_agent(
        agentId=agent_id,
        agentAliasId='LFTSTCQMTR',
        sessionId=f'session-{customer_id}',
        inputText=f'Get customer {customer_id} details'
    )
    
    # Step 2: Analyze issue
    response = agent_client.invoke_agent(
        agentId=agent_id,
        agentAliasId='LFTSTCQMTR',
        sessionId=f'session-{customer_id}',
        inputText=f'Analyze this {issue_type} issue and suggest solutions'
    )
    
    # Step 3: Take action
    response = agent_client.invoke_agent(
        agentId=agent_id,
        agentAliasId='LFTSTCQMTR',
        sessionId=f'session-{customer_id}',
        inputText='Apply the best solution'
    )
    
    return response
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-6.ipynb)

