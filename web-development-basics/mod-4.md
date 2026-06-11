# JavaScript Basics

**Duration:** 15 min

## Core Principles

JavaScript Basics builds on fundamental concepts that form the foundation of web-development-basics. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering JavaScript Basics is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every web-development-basics practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how JavaScript Basics connects to other components in web-development-basics helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply JavaScript Basics in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement JavaScript Basics for their web-development-basics system. They:
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

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What is the difference between let and const?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q3847291" value="0">
      <span>let is for strings, const is for numbers</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q3847291" value="1">
      <span>const is older syntax than let</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q3847291" value="2">
      <span>const cannot be reassigned, let can</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q3847291" value="3">
      <span>They are exactly the same</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What does the === operator check?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7294856" value="0">
      <span>Loose equality (type coercion allowed)</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7294856" value="1">
      <span>Strict equality (same value and type)</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7294856" value="2">
      <span>Assignment of values</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7294856" value="3">
      <span>Greater than or equal to</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What will this code output? let x = 5; x += 3; console.log(x);</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8561729" value="0">
      <span>8</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8561729" value="1">
      <span>5</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8561729" value="2">
      <span>3</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8561729" value="3">
      <span>53</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which arrow function is correct?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4729183" value="0">
      <span>const add = (a, b) { return a + b; }</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4729183" value="1">
      <span>const add = (a, b) -> a + b;</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4729183" value="2">
      <span>const add = (a, b) => a + b;</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4729183" value="3">
      <span>const add = (a, b) => { a + b }</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

Variables have scope - where they can be accessed:

```javascript
// Global scope
let global = "I'm global";

function outer() {
  // Function scope
  let local = "I'm local";
  
  function inner() {
    // Inner function scope
    let innerVar = "I'm inner";
    console.log(global);      // Can access global
    console.log(local);       // Can access outer's local
  }
  
  inner();
  // console.log(innerVar);   // Error: not accessible
}

// Closure: inner function remembers outer scope
function makeCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

let counter = makeCounter();
console.log(counter());       // 1
console.log(counter());       // 2
```

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ What does the map() method do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9183472" value="0">
      <span>Finds the first element matching a condition</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9183472" value="1">
      <span>Removes elements from an array</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9183472" value="2">
      <span>Sorts array elements</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9183472" value="3">
      <span>Transforms each element and returns a new array</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/web-development-basics/mod-4.ipynb)

