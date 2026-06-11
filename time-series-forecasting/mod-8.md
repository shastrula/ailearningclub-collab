# Introduction to Prophet

**Duration:** 15 min

## Core Principles

Introduction to Prophet builds on fundamental concepts that form the foundation of time-series-forecasting. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering Introduction to Prophet is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every time-series-forecasting practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how Introduction to Prophet connects to other components in time-series-forecasting helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply Introduction to Prophet in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement Introduction to Prophet for their time-series-forecasting system. They:
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

Prophet can incorporate holidays and seasonal effects into its forecasts. By specifying holidays, you can improve the accuracy of your forecasts, especially for data that is influenced by specific events or days of the year.

```python title="example2.py"
import pandas as pd
from fbprophet import Prophet

# Sample data
df = pd.DataFrame({'ds': pd.date_range(start='2020-01-01', periods=100, freq='D'), 'y': range(100)})

# Define holidays
holidays = pd.DataFrame({'holiday': 'new_year', 'ds': pd.to_datetime(['2020-01-01'])})

# Initialize the model with holidays
model = Prophet(holidays=holidays)

# Fit the model
model.fit(df)

# Create future dataframe
future = model.make_future_dataframe(periods=30)

# Make predictions
forecast = model.predict(future)

# Print the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```

> **💡 Tip:** When using Prophet, ensure your date column is named 'ds' and your target variable is named 'y'. This is a requirement for the library to function correctly.

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the primary advantage of using Prophet for time series forecasting?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387084288" value="0">
      <span>It requires minimal data preprocessing</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387084288" value="1">
      <span>It can handle multiple seasonalities and holidays</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387084288" value="2">
      <span>It is faster than other forecasting methods</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387084288" value="3">
      <span>It does not require any historical data</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which of the following is a required column name in your dataset when using Prophet?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081280" value="0">
      <span>date</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081280" value="1">
      <span>target</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081280" value="2">
      <span>ds</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387081280" value="3">
      <span>value</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/time-series-forecasting/mod-8.ipynb)

