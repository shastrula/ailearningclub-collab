# File I/O & NIO

**Duration:** 15 min

## Overview

File I/O & NIO is a critical component of java-programming that professionals encounter regularly in production systems.

## Core Concepts

Understanding File I/O & NIO requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where File I/O & NIO connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing File I/O & NIO effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply File I/O & NIO in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - File I/O & NIO behaves differently at scale
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

NIO makes it easy to copy and move files with various options.

```java title="FileCopyMove.java"
import java.nio.file.*;

public class FileCopyMove {
    public static void main(String[] args) throws Exception {
        Path source = Paths.get("source.txt");
        Path copy = Paths.get("copy.txt");
        Path destination = Paths.get("moved.txt");
        
        // Create source file
        Files.writeString(source, "Original content");
        
        // Copy file
        Files.copy(source, copy, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("File copied");
        
        // Move file
        Files.move(copy, destination, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("File moved");
        
        // Verify
        System.out.println("Source exists: " + Files.exists(source));
        System.out.println("Destination exists: " + Files.exists(destination));
    }
}
```

```
File copied
File moved
Source exists: true
Destination exists: true
```

<div class="quiz">
  <p class="font-semibold mb-3">❓ Which class is used to read text files line by line in traditional I/O?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="0">
      <span>FileReader</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="1">
      <span>BufferedReader</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="2">
      <span>FileInputStream</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4829374" value="3">
      <span>Scanner</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What is the main advantage of try-with-resources?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5937284" value="0">
      <span>It makes code run faster</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5937284" value="1">
      <span>It allows multiple catch blocks</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5937284" value="2">
      <span>It automatically closes resources</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q5937284" value="3">
      <span>It prevents exceptions</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ Which NIO class represents a file or directory path?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6284957" value="0">
      <span>Path</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6284957" value="1">
      <span>File</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6284957" value="2">
      <span>Channel</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q6284957" value="3">
      <span>Buffer</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ What does Files.readAllLines() return?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="0">
      <span>A single string with all content</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="1">
      <span>A byte array</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="2">
      <span>A stream of lines</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q7392847" value="3">
      <span>A list of strings</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz">
  <p class="font-semibold mb-3">❓ Which method is used to list files in a directory using NIO?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8473629" value="0">
      <span>Files.list()</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8473629" value="1">
      <span>Files.newDirectoryStream()</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8473629" value="2">
      <span>Path.listFiles()</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q8473629" value="3">
      <span>Files.getDirectoryContents()</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Learn more: https://docs.oracle.com/javase/tutorial/i18n/resbundle/propfile.html
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/java-programming/mod-28.ipynb)

