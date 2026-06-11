# Bedrock with LangChain

**Duration:** 15 min

## Overview

Bedrock with LangChain is a critical component of aws-bedrock that professionals encounter regularly in production systems.

## Core Concepts

Understanding Bedrock with LangChain requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Bedrock with LangChain connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Bedrock with LangChain effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Bedrock with LangChain in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Bedrock with LangChain behaves differently at scale
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
from langchain_aws import ChatBedrock
from langchain.schema import HumanMessage, AIMessage

# Initialize ChatBedrock
chat = ChatBedrock(
    model_id='anthropic.claude-3-sonnet-20240229-v1:0',
    region_name='us-east-1',
    model_kwargs={
        'temperature': 0.7,
        'max_tokens': 1024
    }
)

# Single message
response = chat.invoke([
    HumanMessage(content='What is AWS Bedrock?')
])
print(response.content)

# Multi-turn conversation
messages = [
    HumanMessage(content='What is machine learning?'),
    AIMessage(content='Machine learning is a subset of AI...'),
    HumanMessage(content='Give me an example')
]

response = chat.invoke(messages)
print(response.content)
```

```python
from langchain_aws import BedrockEmbeddings

# Initialize embeddings
embeddings = BedrockEmbeddings(
    model_id='amazon.titan-embed-text-v2:0',
    region_name='us-east-1'
)

# Generate embedding for text
text = 'AWS Bedrock is a managed service'
embedding = embeddings.embed_query(text)
print(f'Embedding dimension: {len(embedding)}')

# Embed multiple texts
texts = [
    'AWS Bedrock',
    'Foundation models',
    'Machine learning'
]
embeddings_list = embeddings.embed_documents(texts)
print(f'Generated {len(embeddings_list)} embeddings')
```

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create a prompt template
prompt = PromptTemplate(
    input_variables=['topic'],
    template='Explain {topic} in simple terms for beginners.'
)

# Create a chain
chain = LLMChain(llm=chat, prompt=prompt)

# Run the chain
result = chain.run(topic='Artificial Intelligence')
print(result)
```

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Create memory
memory = ConversationBufferMemory()

# Create conversation chain with memory
conversation = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=True
)

# Multi-turn conversation
response1 = conversation.run(input='Hi, my name is Alice')
print(response1)

response2 = conversation.run(input='What is my name?')
print(response2)  # Model remembers "Alice"

# View conversation history
print(memory.buffer)
```

```python
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# Load documents
loader = TextLoader('company_docs.txt')
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Create vector store
vector_store = FAISS.from_documents(chunks, embeddings)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type='stuff',
    retriever=vector_store.as_retriever(search_kwargs={'k': 5})
)

# Query
result = qa_chain.run('What is the vacation policy?')
print(result)
```


## Quiz

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the primary purpose of LangChain?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="0">
      <span>To replace Bedrock</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="1">
      <span>To provide abstractions for building LLM applications</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="2">
      <span>To train custom models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7384629" value="3">
      <span>To filter harmful content</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What does ConversationBufferMemory do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="0">
      <span>Stores embeddings</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="1">
      <span>Caches model responses</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="2">
      <span>Maintains conversation history for multi-turn interactions</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="3">
      <span>Filters harmful content</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is a Chain in LangChain?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="0">
      <span>A sequence of operations combining prompts, models, and tools</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="1">
      <span>A blockchain for storing model outputs</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="2">
      <span>A connection to multiple models</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9374628" value="3">
      <span>A security mechanism</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ How do you implement RAG with LangChain?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="0">
      <span>Use only the ChatBedrock class</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="1">
      <span>Combine embeddings, vector store, and RetrievalQA chain</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="2">
      <span>Use Bedrock Knowledge Bases only</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6384729" value="3">
      <span>RAG is not supported in LangChain</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/aws-bedrock/mod-9.ipynb)

