# Site Reliability Engineering

**Duration:** 15 min

## Overview

Site Reliability Engineering is a critical component of devops-platform-engineering that professionals encounter regularly in production systems.

## Core Concepts

Understanding Site Reliability Engineering requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Site Reliability Engineering connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Site Reliability Engineering effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Site Reliability Engineering in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Site Reliability Engineering behaves differently at scale
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
# Calculate error budget
slo_target = 0.999  # 99.9% availability
time_period_seconds = 30 * 24 * 60 * 60  # 30 days

# Maximum allowed downtime
max_downtime = time_period_seconds * (1 - slo_target)
max_downtime_minutes = max_downtime / 60

print(f"Error budget: {max_downtime_minutes:.2f} minutes per month")
# Output: Error budget: 43.20 minutes per month

# Track error budget consumption
current_downtime = 15  # minutes
remaining_budget = max_downtime_minutes - current_downtime
budget_percentage = (remaining_budget / max_downtime_minutes) * 100

print(f"Remaining budget: {remaining_budget:.2f} minutes ({budget_percentage:.1f}%)")
# Output: Remaining budget: 28.20 minutes (65.3%)
```

```python
# Chaos experiment using Chaos Toolkit
from chaoslib.action import action
from chaoslib.exceptions import ActivityFailed

@action
def terminate_random_pod(namespace: str = "production"):
    """Terminate a random pod to test resilience"""
    import subprocess
    
    # Get random pod
    result = subprocess.run(
        f"kubectl get pods -n {namespace} -o jsonpath='{{.items[0].metadata.name}}'",
        shell=True,
        capture_output=True,
        text=True
    )
    
    pod_name = result.stdout.strip()
    
    # Delete pod
    subprocess.run(
        f"kubectl delete pod {pod_name} -n {namespace}",
        shell=True
    )
    
    return {"deleted_pod": pod_name}

@action
def inject_latency(service: str, latency_ms: int = 500):
    """Inject latency into service"""
    # Use Istio VirtualService to inject latency
    pass

@action
def simulate_database_failure():
    """Simulate database connection failure"""
    # Block database traffic using network policies
    pass
```

```python
# SRE-focused metrics
import prometheus_client

# Request metrics
request_duration = prometheus_client.Histogram(
    'request_duration_seconds',
    'Request duration',
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

request_errors = prometheus_client.Counter(
    'request_errors_total',
    'Total request errors',
    ['error_type']
)

# System metrics
uptime = prometheus_client.Gauge(
    'uptime_seconds',
    'Service uptime'
)

# Business metrics
transactions_processed = prometheus_client.Counter(
    'transactions_processed_total',
    'Total transactions processed'
)

# SLO tracking
slo_compliance = prometheus_client.Gauge(
    'slo_compliance_percentage',
    'SLO compliance percentage',
    ['service', 'slo_name']
)

# Usage
request_duration.observe(0.25)
request_errors.labels(error_type='timeout').inc()
slo_compliance.labels(service='api', slo_name='availability').set(99.95)
```


## Quiz

```yaml
# On-call schedule
schedule:
  - week: 1
    primary: alice
    secondary: bob
    escalation: charlie
  
  - week: 2
    primary: bob
    secondary: charlie
    escalation: alice

# On-call responsibilities
responsibilities:
  - Monitor alerts and dashboards
  - Respond to incidents within 5 minutes
  - Follow runbooks for common issues
  - Escalate to technical lead if needed
  - Document all actions taken
  - Participate in postmortems

# On-call support
support:
  - Slack channel: #on-call
  - Pagerduty integration for alerts
  - Runbooks available in wiki
  - Escalation contacts documented
```

---

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is an SLO (Service Level Objective)?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="0">
      <span>A target for service performance (e.g., 99.9% availability)</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="1">
      <span>A measurable metric of service performance</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="2">
      <span>A contractual commitment with customers</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="3">
      <span>A monitoring tool</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is an error budget?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="0">
      <span>The cost of fixing errors</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="1">
      <span>The number of bugs allowed in code</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="2">
      <span>The acceptable amount of downtime or errors within an SLO</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="3">
      <span>A financial allocation for operations</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the purpose of a blameless postmortem?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="0">
      <span>To identify who caused the incident</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="1">
      <span>To learn from incidents and prevent recurrence</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="2">
      <span>To punish team members</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284736" value="3">
      <span>To document system architecture</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is chaos engineering?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="0">
      <span>Proactively testing system resilience by injecting failures</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="1">
      <span>Randomly breaking production systems</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="2">
      <span>A type of security attack</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7463829" value="3">
      <span>Disorganized incident response</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the primary goal of SRE?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="0">
      <span>To eliminate all system failures</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="1">
      <span>To balance reliability with velocity using error budgets</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="2">
      <span>To replace developers with automation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8374629" value="3">
      <span>To maximize uptime at any cost</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/devops-platform-engineering/mod-12.ipynb)

