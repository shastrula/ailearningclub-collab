# HTML Fundamentals

**Duration:** 15 min

## Core Principles

HTML Fundamentals builds on fundamental concepts that form the foundation of web-development-basics. Understanding these principles deeply will help you grasp advanced topics later.

The key to mastering HTML Fundamentals is recognizing the underlying patterns. These patterns repeat across different contexts, making them valuable mental models for solving diverse problems.

## Essential Concepts

**Concept 1: Foundation** - Every web-development-basics practitioner must understand this core idea. It appears consistently in industry practice, academic research, and real-world applications. Once you internalize this concept, you'll see it everywhere.

**Concept 2: Application** - This principle explains how the theory translates into practical systems. Most engineers encounter this concept when scaling from prototypes to production systems.

**Concept 3: Integration** - Understanding how HTML Fundamentals connects to other components in web-development-basics helps you make informed architectural decisions.

## Practical Implementation

Here's how practitioners apply HTML Fundamentals in real scenarios:

1. Start with the basics and build incrementally
2. Understand each component before combining them
3. Follow established patterns that teams have validated
4. Test your assumptions with data, not intuition
5. Monitor for issues that arise in production

## Real-World Example

Consider a typical scenario: A team needs to implement HTML Fundamentals for their web-development-basics system. They:
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

Images are embedded with the `<img>` tag. Always include an `alt` attribute for accessibility:

```html
<img src="photo.jpg" alt="A beautiful sunset" width="400" height="300">

<picture>
  <source media="(max-width: 600px)" srcset="small.jpg">
  <source media="(min-width: 601px)" srcset="large.jpg">
  <img src="default.jpg" alt="Responsive image">
</picture>

<video width="400" controls>
  <source src="video.mp4" type="video/mp4">
  Your browser doesn't support HTML5 video.
</video>

<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  Your browser doesn't support HTML5 audio.
</audio>
```

---

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What does HTML stand for?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q2847561" value="0">
      <span>HyperText Markup Language</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q2847561" value="1">
      <span>High Tech Markup Language</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q2847561" value="2">
      <span>Home Tool Markup Language</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q2847561" value="3">
      <span>Hyperlinks and Text Markup Language</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which tag is used for the main content of a page?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6392847" value="0">
      <span>&lt;body&gt;</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6392847" value="1">
      <span>&lt;section&gt;</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6392847" value="2">
      <span>&lt;main&gt;</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6392847" value="3">
      <span>&lt;article&gt;</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the purpose of the alt attribute in images?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7561294" value="0">
      <span>To set the image size</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7561294" value="1">
      <span>To provide alternative text for accessibility</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7561294" value="2">
      <span>To add a border around the image</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7561294" value="3">
      <span>To link to another page</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ Which attribute specifies where a form should send its data?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829371" value="0">
      <span>action</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829371" value="1">
      <span>method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829371" value="2">
      <span>target</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829371" value="3">
      <span>submit</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

---

<div class="quiz" data-correct="3">
  <p class="font-semibold mb-3">❓ What is semantic HTML?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="0">
      <span>HTML that uses only div tags</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="1">
      <span>HTML that is minified for performance</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="2">
      <span>HTML that uses inline styles</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q9284756" value="3">
      <span>HTML that uses tags describing their meaning</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/web-development-basics/mod-2.ipynb)

