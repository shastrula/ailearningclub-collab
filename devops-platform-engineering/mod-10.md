# Security & Compliance

**Duration:** 15 min

## Overview

Security & Compliance is a critical component of devops-platform-engineering that professionals encounter regularly in production systems.

## Core Concepts

Understanding Security & Compliance requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Security & Compliance connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Security & Compliance effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Security & Compliance in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Security & Compliance behaves differently at scale
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

secrets_client = boto3.client('secretsmanager')

def get_db_credentials():
    response = secrets_client.get_secret_value(
        SecretId='prod/db-password'
    )
    secret = json.loads(response['SecretString'])
    return secret['username'], secret['password']

username, password = get_db_credentials()
```


## Quiz

```bash
# Scan Docker image with Trivy
trivy image myapp:latest

# Scan Kubernetes manifests
trivy config ./k8s/

# Scan filesystem
trivy fs ./src/

# Generate SBOM (Software Bill of Materials)
trivy image --format cyclonedx myapp:latest > sbom.json
```

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is AWS IAM used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="0">
      <span>Managing EC2 instances</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="1">
      <span>Controlling access to AWS resources</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="2">
      <span>Monitoring application performance</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="3">
      <span>Managing DNS records</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is AWS Secrets Manager used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="0">
      <span>Securely storing and rotating secrets</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="1">
      <span>Managing IAM policies</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="2">
      <span>Encrypting S3 buckets</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="3">
      <span>Monitoring security events</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What does AWS GuardDuty do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="0">
      <span>Manages firewall rules</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="1">
      <span>Encrypts data at rest</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="2">
      <span>Detects threats using machine learning</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="3">
      <span>Manages SSL certificates</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the principle of least privilege?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="0">
      <span>Grant all permissions to all users</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="1">
      <span>Grant only the minimum permissions needed</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="2">
      <span>Deny all access by default</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="3">
      <span>Use the same password for all accounts</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is CloudTrail used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="0">
      <span>Audit logging of AWS API calls</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="1">
      <span>Managing network traffic</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="2">
      <span>Encrypting data in transit</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="3">
      <span>Managing SSL certificates</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/devops-platform-engineering/mod-10.ipynb)

