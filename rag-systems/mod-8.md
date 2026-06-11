# LangChain Basics

**Duration:** 15 min

## Core Principles

LangChain Basics builds on fundamental concepts that form the foundation of rag-systems. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering LangChain Basics is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every rag-systems practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how LangChain Basics connects to other components in rag-systems helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply LangChain Basics in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement LangChain Basics for their rag-systems system. They:
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
from sentence_transformers import SentenceTransformer

# Load a pre-trained model for creating embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to create embeddings
def create_embedding(text):
    return model.encode(text)

text = "Hello, world!"
embedding = create_embedding(text)
print(embedding)
```

```python
import random
import spacy

# Load a pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to chunk text
def chunk_text(text, chunk_size=100):
    doc = nlp(text)
    return [doc[i:i+chunk_size] for i in range(0, len(doc), chunk_size)]

# Function to rerank results
def rerank_results(results):
    # Placeholder for a more complex reranking algorithm
    return sorted(results, key=lambda x: random.random())

text = "This is a long document that needs to be chunked and reranked."
chunks = chunk_text(text)
reranked_chunks = rerank_results(chunks)
print(reranked_chunks)
```

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
import numpy as np

# Load a pre-trained model for creating embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to perform hybrid search
def hybrid_search(query, documents, top_k=5):
    # Keyword-based search using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    query_vec = vectorizer.transform([query])
    keyword_scores = (tfidf_matrix * query_vec.T).toarray().flatten()
    
    # Semantic search using embeddings
    document_embeddings = model.encode(documents)
    query_embedding = model.encode(query)
    semantic_scores = 1 - np.linalg.norm(document_embeddings - query_embedding, axis=1)
    
    # Combine scores
    combined_scores = keyword_scores + semantic_scores
    top_indices = np.argsort(combined_scores)[-top_k:]
    return [documents[i] for i in top_indices]

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A quick brown dog jumps over the lazy fox.",
    "The lazy fox is jumped over by the quick brown dog."
]
query = "quick fox"
results = hybrid_search(query, documents)
print(results)
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/rag-systems/mod-8.ipynb)

