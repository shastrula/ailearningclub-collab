# Combining Vector and Keyword Search

**Duration:** 15 min

## Overview

Combining Vector and Keyword Search is a critical component of rag-systems that professionals encounter regularly in production systems.

## Core Concepts

Understanding Combining Vector and Keyword Search requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Combining Vector and Keyword Search connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Combining Vector and Keyword Search effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Combining Vector and Keyword Search in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Combining Vector and Keyword Search behaves differently at scale
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = ["The cat sat on the mat.", "The dog played in the park.", "The cat chased the mouse."]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert to dense array for simplicity
tfidf_matrix_dense = tfidf_matrix.toarray()

# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix_dense)

print(similarity_matrix)
```

```python
from collections import defaultdict

# Sample documents
documents = ["The cat sat on the mat.", "The dog played in the park.", "The cat chased the mouse."]

# Create an inverted index
index = defaultdict(list)

for doc_id, doc in enumerate(documents):
    words = doc.lower().split()
    for word in words:
        index[word].append(doc_id)

# Search for a keyword
keyword = "cat"
results = index[keyword.lower()]

print(f"Documents containing '{keyword}': {results}")
```

```python
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

# Sample documents
documents = ["The cat sat on the mat.", "The dog played in the park.", "The cat chased the mouse."]

# Keyword search
index = defaultdict(list)
for doc_id, doc in enumerate(documents):
    words = doc.lower().split()
    for word in words:
        index[word].append(doc_id)

# Vector search
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
tfidf_matrix_dense = tfidf_matrix.toarray()

# Query
query = "cat"
keyword_results = index[query.lower()]
query_vector = vectorizer.transform([query]).toarray()

# Combine results
combined_scores = {}
for doc_id in keyword_results:
    similarity_score = cosine_similarity(query_vector, tfidf_matrix_dense[doc_id])
    combined_scores[doc_id] = similarity_score[0][0]

# Sort by combined scores
sorted_results = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_results)
```


## Quiz

### Quiz 1: What is the primary advantage of using vector search over keyword search?
- [ ] It requires less computational resources
- [✓] It understands context and relationships between words
- [ ] It is faster for large datasets
- [ ] It does not require any preprocessing

### Quiz 2: Which method is better suited for retrieving documents containing specific terms?
- [ ] Vector search
- [✓] Keyword search
- [ ] Hybrid search
- [ ] LangChain

### Quiz 3: How can you combine vector and keyword search effectively?
- [ ] Use vector search alone
- [ ] Use keyword search alone
- [✓] Use a hybrid approach by filtering with keyword search and ranking with vector search
- [ ] Ignore both methods
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/rag-systems/mod-11.ipynb)

