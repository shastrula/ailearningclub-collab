# Stacking Ensembles: Basics

**Duration:** 15 min

## Core Principles

Stacking Ensembles: Basics builds on fundamental concepts that form the foundation of ensemble-learning. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering Stacking Ensembles: Basics is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every ensemble-learning practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how Stacking Ensembles: Basics connects to other components in ensemble-learning helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply Stacking Ensembles: Basics in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement Stacking Ensembles: Basics for their ensemble-learning system. They:
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


## Quiz

To avoid overfitting and ensure robust performance, it's essential to use cross-validation when training the base models. This involves splitting the training data into multiple folds, training each base model on different folds, and using the out-of-fold predictions as input for the meta-model. This approach helps generalize the stacking ensemble better.

```python title="example2.py"
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
    ('lr', LogisticRegression(random_state=42))
]

# Initialize KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize arrays to hold out-of-fold predictions
base_model_predictions = np.zeros((len(X_train), len(base_models)))

# Train base models with cross-validation
for idx, (name, model) in enumerate(base_models):
    for train_index, val_index in kf.split(X_train):
        X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
        y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
        model.fit(X_fold_train, y_fold_train)
        base_model_predictions[val_index, idx] = model.predict(X_fold_val)

# Train meta-model on out-of-fold predictions
meta_model = LogisticRegression(random_state=42)
meta_model.fit(base_model_predictions, y_train)

# Make final prediction
final_predictions = meta_model.predict(base_model_predictions)

# Evaluate performance
accuracy = accuracy_score(y_train, final_predictions)
print(f'Stacking Ensemble Accuracy (Cross-Validation): {accuracy:.2f}')
```

> **💡 Tip:** When implementing stacking, ensure that the base models are sufficiently diverse to capture different aspects of the data. Using cross-validation for training the base models helps prevent overfitting and improves the generalization of the stacking ensemble.

To avoid overfitting and ensure robust performance, it's essential to use cross-validation when training the base models. This involves splitting the training data into multiple folds, training each base model on different folds, and using the out-of-fold predictions as input for the meta-model. This approach helps generalize the stacking ensemble better.

```python title="example2.py"
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
    ('lr', LogisticRegression(random_state=42))
]

# Initialize KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize arrays to hold out-of-fold predictions
base_model_predictions = np.zeros((len(X_train), len(base_models)))

# Train base models with cross-validation
for idx, (name, model) in enumerate(base_models):
    for train_index, val_index in kf.split(X_train):
        X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
        y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
        model.fit(X_fold_train, y_fold_train)
        base_model_predictions[val_index, idx] = model.predict(X_fold_val)

# Train meta-model on out-of-fold predictions
meta_model = LogisticRegression(random_state=42)
meta_model.fit(base_model_predictions, y_train)

# Make final prediction
final_predictions = meta_model.predict(base_model_predictions)

# Evaluate performance
accuracy = accuracy_score(y_train, final_predictions)
print(f'Stacking Ensemble Accuracy (Cross-Validation): {accuracy:.2f}')
```

>
  <p class="font-semibold mb-3">❓ What is the primary goal of stacking ensembles?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387093888" value="0">
      <span>To reduce model complexity</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387093888" value="1">
      <span>To improve predictive performance by combining multiple models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387093888" value="2">
      <span>To increase model interpretability</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387093888" value="3">
      <span>To decrease training time</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

To avoid overfitting and ensure robust performance, it's essential to use cross-validation when training the base models. This involves splitting the training data into multiple folds, training each base model on different folds, and using the out-of-fold predictions as input for the meta-model. This approach helps generalize the stacking ensemble better.

```python title="example2.py"
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
    ('lr', LogisticRegression(random_state=42))
]

# Initialize KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize arrays to hold out-of-fold predictions
base_model_predictions = np.zeros((len(X_train), len(base_models)))

# Train base models with cross-validation
for idx, (name, model) in enumerate(base_models):
    for train_index, val_index in kf.split(X_train):
        X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
        y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
        model.fit(X_fold_train, y_fold_train)
        base_model_predictions[val_index, idx] = model.predict(X_fold_val)

# Train meta-model on out-of-fold predictions
meta_model = LogisticRegression(random_state=42)
meta_model.fit(base_model_predictions, y_train)

# Make final prediction
final_predictions = meta_model.predict(base_model_predictions)

# Evaluate performance
accuracy = accuracy_score(y_train, final_predictions)
print(f'Stacking Ensemble Accuracy (Cross-Validation): {accuracy:.2f}')
```

>
  <p class="font-semibold mb-3">❓ Why is cross-validation important in stacking ensembles?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081152" value="0">
      <span>To increase model complexity</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081152" value="1">
      <span>To ensure robust performance and avoid overfitting</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081152" value="2">
      <span>To reduce the number of base models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081152" value="3">
      <span>To speed up the training process</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/ensemble-learning/mod-14.ipynb)

