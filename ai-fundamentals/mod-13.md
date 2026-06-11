# Reinforcement Learning Fundamentals

**Duration:** 15 min

## Core Principles

Reinforcement Learning Fundamentals builds on fundamental concepts that form the foundation of ai-fundamentals. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering Reinforcement Learning Fundamentals is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every ai-fundamentals practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how Reinforcement Learning Fundamentals connects to other components in ai-fundamentals helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply Reinforcement Learning Fundamentals in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement Reinforcement Learning Fundamentals for their ai-fundamentals system. They:
- Defined requirements clearly
- Chose an appropriate design pattern
- Implemented core functionality
- Added error handling and monitoring
- Deployed gradually to production

Their results demonstrate that following these principles leads to reliable systems.

## Common Challenges

Practitioners often encounter these issues:
- Underestimating complexity early on
- Insufficient testing before deployment
- Inadequate monitoring in production
- Not planning for future changes

Recognizing these patterns helps you avoid repeating them.

## Best Practices Summary

- Keep implementations simple until complexity is truly necessary
- Always measure before optimizing
- Document your design decisions for future maintainers
- Build monitoring into your system from the start
- Plan for updates and operational maintenance


## Code Examples

```python
import numpy as np

# Define the states, actions, and transition probabilities
states = ['A', 'B', 'C']
actions = ['left', 'right']
transition_probs = {
    ('A', 'left'): {'A': 1.0},
    ('A', 'right'): {'B': 0.8, 'C': 0.2},
    ('B', 'left'): {'A': 0.6, 'B': 0.4},
    ('B', 'right'): {'C': 1.0},
    ('C', 'left'): {'B': 1.0},
    ('C', 'right'): {'C': 1.0}
}

# Define the rewards
rewards = {
    ('A', 'left', 'A'): 0,
    ('A', 'right', 'B'): 1,
    ('A', 'right', 'C'): -1,
    ('B', 'left', 'A'): 0.5,
    ('B', 'left', 'B'): -0.5,
    ('B', 'right', 'C'): 2,
    ('C', 'left', 'B'): 0,
    ('C', 'right', 'C'): 0
}

# Value iteration algorithm
V = {s: 0 for s in states}
gamma = 0.9

for _ in range(1000):
    V_new = V.copy()
    for s in states:
        V_new[s] = max(
            sum(transition_probs[s, a][s_] * (rewards[s, a, s_] + gamma * V[s_]) for s_ in transition_probs[s, a])
            for a in actions
        )
    V = V_new

print('Optimal value function:', V)
```

```python
import numpy as np
import random

# Define the environment
states = ['A', 'B', 'C']
actions = ['left', 'right']
rewards = {
    ('A', 'left'): 0,
    ('A', 'right'): 1,
    ('B', 'left'): 0.5,
    ('B', 'right'): 2,
    ('C', 'left'): 0,
    ('C', 'right'): 0
}

# Initialize Q-table
Q = np.zeros((len(states), len(actions)))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Q-Learning algorithm
for episode in range(1000):
    state = random.choice(states)
    done = False
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  # Explore
        else:
            action = actions[np.argmax(Q[states.index(state), :])]  # Exploit
        next_state = random.choice([s for s in states if s!= state])
        reward = rewards[(state, action)]
        best_next_action = np.argmax(Q[states.index(next_state), :])
        Q[states.index(state), actions.index(action)] += alpha * (
            reward + gamma * Q[states.index(next_state), best_next_action] - 
            Q[states.index(state), actions.index(action)]
        )
        state = next_state
        if state == 'C':
            done = True

print('Optimal Q-table:', Q)
```


## Quiz

### Quiz 1: What is the primary goal in a Markov Decision Process (MDP)?
- [ ] To minimize the expected cumulative reward
- [✓] To maximize the expected cumulative reward
- [ ] To find the shortest path between states
- [ ] To balance exploration and exploitation

### Quiz 2: Which of the following is a characteristic of Q-Learning?
- [ ] It requires a model of the environment
- [✓] It is a model-free reinforcement learning algorithm
- [ ] It uses a value function to estimate the expected reward
- [ ] It is used primarily for supervised learning tasks

### Quiz 3: What is the role of the Q-table in Q-Learning?
- [ ] It stores the transition probabilities between states
- [✓] It stores the expected utility of taking a given action in a given state
- [ ] It stores the immediate rewards for each state-action pair
- [ ] It stores the policy for the agent
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/ai-fundamentals/mod-13.ipynb)

