# Calculus & Gradient Descent: How Models Learn

**Duration:** 15 min

## Overview

Calculus & Gradient Descent: How Models Learn is a critical component of maths-and-statistics-in-ai that professionals encounter regularly in production systems.

## Core Concepts

Understanding Calculus & Gradient Descent: How Models Learn requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Calculus & Gradient Descent: How Models Learn connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Calculus & Gradient Descent: How Models Learn effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Calculus & Gradient Descent: How Models Learn in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Calculus & Gradient Descent: How Models Learn behaves differently at scale
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
import numpy as np

def numerical_gradient(loss_fn, theta, epsilon=1e-5):
    """Compute gradient by finite differences"""
    grad = np.zeros_like(theta)
    for i in range(len(theta)):
        theta_plus = theta.copy()
        theta_plus[i] += epsilon
        theta_minus = theta.copy()
        theta_minus[i] -= epsilon
        grad[i] = (loss_fn(theta_plus) - loss_fn(theta_minus)) / (2 * epsilon)
    return grad

# Example: minimize f(x) = x^2
def f(x):
    return np.sum(x**2)

theta = np.array([3.0, 4.0])
grad = numerical_gradient(f, theta)
print(f"Gradient at {theta}: {grad}")  # [6.0, 8.0] (correct: 2*x)
```

```python
import torch

# Define a simple network
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 3*x + 1

# Compute gradient automatically
y.backward()
print(f"dy/dx at x=2: {x.grad}")  # 7.0 (correct: 2*2 + 3)

# For a neural network
model = torch.nn.Linear(10, 1)
x = torch.randn(32, 10)
y_true = torch.randn(32, 1)

# Forward pass
y_pred = model(x)
loss = torch.nn.functional.mse_loss(y_pred, y_true)

# Backward pass (compute gradients)
loss.backward()

# Gradients are now in model.weight.grad and model.bias.grad
print(f"Weight gradient shape: {model.weight.grad.shape}")
```

```python
import torch
import torch.optim as optim

model = torch.nn.Linear(10, 1)
optimizer = optim.SGD(model.parameters(), lr=0.01)  # lr = learning rate

for epoch in range(100):
    # Forward pass
    y_pred = model(x)
    loss = torch.nn.functional.mse_loss(y_pred, y_true)
    
    # Backward pass
    optimizer.zero_grad()  # Clear old gradients
    loss.backward()        # Compute new gradients
    
    # Update weights
    optimizer.step()       # theta = theta - lr * grad
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

```python
# Adam = Adaptive Moment Estimation
# Combines momentum with adaptive learning rates
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Same training loop as before
for epoch in range(100):
    y_pred = model(x)
    loss = torch.nn.functional.mse_loss(y_pred, y_true)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

```python
from torch.utils.checkpoint import checkpoint

class TransformerBlock(torch.nn.Module):
    def forward(self, x):
        # Without checkpointing: stores all activations
        # x = self.attention(x)
        # x = self.ffn(x)
        
        # With checkpointing: recomputes activations during backward
        x = checkpoint(self.attention, x)
        x = checkpoint(self.ffn, x)
        return x
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/maths-and-statistics-in-ai/mod-2.ipynb)

