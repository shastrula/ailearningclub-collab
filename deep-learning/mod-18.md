# Working with GPUs

**Duration:** 15 min

## Overview

Working with GPUs is a critical component of deep-learning that professionals encounter regularly in production systems.

## Core Concepts

Understanding Working with GPUs requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Working with GPUs connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Working with GPUs effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Working with GPUs in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Working with GPUs behaves differently at scale
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
import torch

# Check if CUDA (GPU support) is available
is_gpu_available = torch.cuda.is_available()

print(f'Is CUDA available: {is_gpu_available}')

# If CUDA is available, print the number of GPUs
if is_gpu_available:
    print(f'Number of GPUs: {torch.cuda.device_count()}')
```

```python
import torch

# Check if CUDA is available
is_gpu_available = torch.cuda.is_available()
device = torch.device('cuda' if is_gpu_available else 'cpu')

# Create a tensor and move it to the GPU
tensor_cpu = torch.tensor([1.0, 2.0, 3.0])
tensor_gpu = tensor_cpu.to(device)

print(f'Tensor on {device}:\n{tensor_gpu}')
```

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Check if CUDA is available
is_gpu_available = torch.cuda.is_available()
device = torch.device('cuda' if is_gpu_available else 'cpu')
print(f'Using device: {device}')
```

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=100, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False, num_workers=2)
```

```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net().to(device)
```


## Quiz

### Quiz 1: How do you check if CUDA is available in PyTorch?
- [ ] torch.is_cuda_available()
- [✓] torch.cuda.is_available()
- [ ] torch.cuda.available()
- [ ] torch.is_available_cuda()

### Quiz 2: What method do you use to move a tensor to the GPU in PyTorch?
- [ ] .to_gpu()
- [ ].cuda()
- [✓] .to(device)
- [ ].move_to_gpu()

### Quiz 3: Why is it important to move both your model and data to the same device (CPU or GPU)?
- [ ] It improves model accuracy.
- [✓] It avoids errors during computation.
- [ ] It reduces memory usage.
- [ ] It speeds up data loading.
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/deep-learning/mod-18.ipynb)

