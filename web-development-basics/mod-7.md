# APIs, Fetch & JSON

**Duration:** 15 min

## Overview

APIs, Fetch & JSON is a critical component of web-development-basics that professionals encounter regularly in production systems.

## Core Concepts

Understanding APIs, Fetch & JSON requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where APIs, Fetch & JSON connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing APIs, Fetch & JSON effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply APIs, Fetch & JSON in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - APIs, Fetch & JSON behaves differently at scale
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


## Quiz

Fetch data and update the page:

```javascript
// Fetch and display user list
async function displayUsers() {
  try {
    let response = await fetch("https://api.example.com/users");
    let users = await response.json();
    
    let list = document.querySelector("#user-list");
    list.innerHTML = "";
    
    users.forEach(user => {
      let item = document.createElement("li");
      item.textContent = `${user.name} (${user.email})`;
      list.appendChild(item);
    });
  } catch (error) {
    console.error("Error:", error);
  }
}

// Call on page load
document.addEventListener("DOMContentLoaded", displayUsers);

// Search functionality
let searchInput = document.querySelector("#search");
searchInput.addEventListener("keyup", async (e) => {
  let query = e.target.value;
  
  try {
    let response = await fetch(`https://api.example.com/users?search=${query}`);
    let results = await response.json();
    
    let list = document.querySelector("#results");
    list.innerHTML = "";
    
    results.forEach(user => {
      let item = document.createElement("div");
      item.innerHTML = `<h3>${user.name}</h3><p>${user.email}</p>`;
      list.appendChild(item);
    });
  } catch (error) {
    console.error("Error:", error);
  }
});

// Form submission with API
let form = document.querySelector("form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  let formData = new FormData(form);
  let userData = Object.fromEntries(formData);
  
  try {
    let response = await fetch("https://api.example.com/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData)
    });
    
    if (response.ok) {
      alert("User created successfully!");
      form.reset();
    }
  } catch (error) {
    console.error("Error:", error);
  }
});
```

---

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What does REST API stand for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="0">
      <span>Representational State Transfer API</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="1">
      <span>Remote Execution Service Transfer API</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="2">
      <span>Real-time Event Streaming API</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="3">
      <span>Rapid Exchange Service Transfer API</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What does JSON stand for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="0">
      <span>Java Script Object Notation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="1">
      <span>JavaScript Object Notation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="2">
      <span>JavaScript Online Notation</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8294756" value="3">
      <span>Java Serialized Object Notation</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which HTTP method is used to create new data?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6729384" value="0">
      <span>GET</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6729384" value="1">
      <span>PUT</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6729384" value="2">
      <span>POST</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6729384" value="3">
      <span>DELETE</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What does response.json() do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5847291" value="0">
      <span>Converts JSON to a string</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5847291" value="1">
      <span>Parses the response body as JSON</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5847291" value="2">
      <span>Checks if the response is valid</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5847291" value="3">
      <span>Sends JSON data to the server</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is async/await used for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="0">
      <span>Handling asynchronous operations with cleaner syntax</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="1">
      <span>Making synchronous code run faster</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="2">
      <span>Preventing errors in JavaScript</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="3">
      <span>Creating new API endpoints</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/web-development-basics/mod-7.ipynb)

