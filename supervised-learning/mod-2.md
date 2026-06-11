# Linear Regression Basics

**Duration:** 15 min

## Core Principles

Linear Regression Basics builds on fundamental concepts that form the foundation of supervised-learning. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering Linear Regression Basics is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every supervised-learning practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how Linear Regression Basics connects to other components in supervised-learning helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply Linear Regression Basics in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement Linear Regression Basics for their supervised-learning system. They:
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

After fitting a Linear Regression model, it's important to evaluate its performance. Common metrics include the coefficient of determination (R^2 score) and Mean Squared Error (MSE). The R^2 score indicates how well the model explains the variance in the target variable, while MSE measures the average squared difference between actual and predicted values.

```python title="example2.py"
from sklearn.metrics import r2_score, mean_squared_error

# Actual and predicted values
y_true = np.array([2, 3, 5, 7, 11])
y_pred = model.predict(x)

# Calculate metrics
r2 = r2_score(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

print(f'R^2 Score: {r2}')
print(f'Mean Squared Error: {mse}')
```

> **💡 Tip:** Always check the assumptions of Linear Regression, such as linearity, independence, homoscedasticity, and normality of residuals, to ensure the model's validity.

After fitting a Linear Regression model, it's important to evaluate its performance. Common metrics include the coefficient of determination (R^2 score) and Mean Squared Error (MSE). The R^2 score indicates how well the model explains the variance in the target variable, while MSE measures the average squared difference between actual and predicted values.

```python title="example2.py"
from sklearn.metrics import r2_score, mean_squared_error

# Actual and predicted values
y_true = np.array([2, 3, 5, 7, 11])
y_pred = model.predict(x)

# Calculate metrics
r2 = r2_score(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

print(f'R^2 Score: {r2}')
print(f'Mean Squared Error: {mse}')
```

>
  <p class="font-semibold mb-3">❓ What is the primary goal of Linear Regression?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386962368" value="0">
      <span>To classify data into categories</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386962368" value="1">
      <span>To predict a continuous outcome</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386962368" value="2">
      <span>To cluster similar data points</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386962368" value="3">
      <span>To reduce the dimensionality of data</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

After fitting a Linear Regression model, it's important to evaluate its performance. Common metrics include the coefficient of determination (R^2 score) and Mean Squared Error (MSE). The R^2 score indicates how well the model explains the variance in the target variable, while MSE measures the average squared difference between actual and predicted values.

```python title="example2.py"
from sklearn.metrics import r2_score, mean_squared_error

# Actual and predicted values
y_true = np.array([2, 3, 5, 7, 11])
y_pred = model.predict(x)

# Calculate metrics
r2 = r2_score(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

print(f'R^2 Score: {r2}')
print(f'Mean Squared Error: {mse}')
```

>
  <p class="font-semibold mb-3">❓ Which metric is used to evaluate how well the Linear Regression model explains the variance in the target variable?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386912576" value="0">
      <span>Mean Absolute Error</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386912576" value="1">
      <span>Root Mean Squared Error</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386912576" value="2">
      <span>Coefficient of Determination (R^2)</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386912576" value="3">
      <span>Adjusted R^2</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/supervised-learning/mod-2.ipynb)

