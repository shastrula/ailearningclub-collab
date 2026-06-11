# Control Flow: Conditionals & Loops

**Duration:** 15 min

## Overview

Control Flow: Conditionals & Loops is a critical component of java-comprehensive that professionals encounter regularly in production systems.

## Core Concepts

Understanding Control Flow: Conditionals & Loops requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Control Flow: Conditionals & Loops connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Control Flow: Conditionals & Loops effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Control Flow: Conditionals & Loops in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Control Flow: Conditionals & Loops behaves differently at scale
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

Control flow determines the order in which statements execute. Java provides if/else for conditionals and for/while loops for repetition. Mastering control flow is essential for writing programs that respond to different conditions and process data efficiently. Understanding how to structure your code with proper control flow makes it more readable and maintainable.

```java title="IfElse.java"
public class IfElse {
    public static void main(String[] args) {
        int age = 20;
        if (age >= 18) System.out.println("Adult");
        else System.out.println("Minor");
    }
}
```



```
Adult
```

```java title="IfElseIf.java"
public class IfElseIf {
    public static void main(String[] args) {
        int score = 75;
        if (score >= 90) System.out.println("A");
        else if (score >= 80) System.out.println("B");
        else if (score >= 70) System.out.println("C");
        else System.out.println("F");
    }
}
```

```
C
```

```java title="Switch.java"
public class Switch {
    public static void main(String[] args) {
        int day = 3;
        switch (day) {
            case 1: System.out.println("Mon"); break;
            case 2: System.out.println("Tue"); break;
            case 3: System.out.println("Wed"); break;
            default: System.out.println("Other");
        }
    }
}
```

```
Wed
```

```java title="ForLoop.java"
public class ForLoop {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) System.out.println(i);
    }
}
```

```
1
2
3
4
5
```

```java title="WhileLoop.java"
public class WhileLoop {
    public static void main(String[] args) {
        int i = 1;
        while (i <= 3) {
            System.out.println(i);
            i++;
        }
    }
}
```

```
1
2
3
```

```java title="DoWhile.java"
public class DoWhile {
    public static void main(String[] args) {
        int i = 1;
        do {
            System.out.println(i);
            i++;
        } while (i <= 3);
    }
}
```

```
1
2
3
```

```java title="BreakContinue.java"
public class BreakContinue {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            if (i == 3) continue;
            if (i == 5) break;
            System.out.println(i);
        }
    }
}
```

```
1
2
4
```

```java title="NestedLoop.java"
public class NestedLoop {
    public static void main(String[] args) {
        for (int i = 1; i <= 2; i++)
            for (int j = 1; j <= 2; j++)
                System.out.println("i=" + i + ", j=" + j);
    }
}
```

```
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
```

```java title="Ternary.java"
public class Ternary {
    public static void main(String[] args) {
        int age = 20;
        String status = (age >= 18) ? "Adult" : "Minor";
        System.out.println(status);
    }
}
```

```
Adult
```

```java title="EnhancedFor.java"
public class EnhancedFor {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        for (int num : nums) System.out.println(num);
    }
}
```

```
1
2
3
4
5
```

```java title="LoopLabels.java"
public class LoopLabels {
    public static void main(String[] args) {
        outer: for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) break outer;
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
```

```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
```

> **💡 Tip:** Best Practice: Use break in switch statements to prevent fall-through to the next case.

> **💡 Tip:** Common Mistake: Infinite loops occur when the loop condition never becomes false. Always ensure your loop has a proper exit condition.

Learn more: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What does the if statement do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387187648" value="0">
      <span>Repeats code</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387187648" value="1">
      <span>Executes code if condition is true</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387187648" value="2">
      <span>Declares a variable</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387187648" value="3">
      <span>Creates a loop</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which keyword is used to exit a loop?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387177536" value="0">
      <span>exit</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387177536" value="1">
      <span>stop</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387177536" value="2">
      <span>break</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387177536" value="3">
      <span>end</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the difference between while and do-while?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192128" value="0">
      <span>No difference</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192128" value="1">
      <span>do-while executes at least once</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192128" value="2">
      <span>while is faster</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192128" value="3">
      <span>do-while is for arrays</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What does continue do in a loop?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192512" value="0">
      <span>Exits the loop</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192512" value="1">
      <span>Skips current iteration</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192512" value="2">
      <span>Restarts the loop</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192512" value="3">
      <span>Pauses the loop</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which statement is used for multiple conditions?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192576" value="0">
      <span>if</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192576" value="1">
      <span>else if</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192576" value="2">
      <span>switch</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387192576" value="3">
      <span>for</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What is the output of the ternary operator (true ? "yes" : "no")?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387182144" value="0">
      <span>true</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387182144" value="1">
      <span>yes</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387182144" value="2">
      <span>no</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387182144" value="3">
      <span>Error</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ How many times does this loop execute: for(int i=0; i<5; i++)?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387183808" value="0">
      <span>4 times</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387183808" value="1">
      <span>5 times</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387183808" value="2">
      <span>6 times</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387183808" value="3">
      <span>Infinite</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="0">
  <p class="font-semibold mb-3">❓ What is a nested loop?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184000" value="0">
      <span>A loop inside another loop</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184000" value="1">
      <span>A loop with multiple conditions</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184000" value="2">
      <span>A loop that repeats</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184000" value="3">
      <span>A loop with break</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="2">
  <p class="font-semibold mb-3">❓ Which loop is best for iterating a fixed number of times?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184512" value="0">
      <span>while</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184512" value="1">
      <span>do-while</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184512" value="2">
      <span>for</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387184512" value="3">
      <span>switch</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

<div class="quiz" data-correct="1">
  <p class="font-semibold mb-3">❓ What happens if you forget break in a switch case?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387185216" value="0">
      <span>Compilation error</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387185216" value="1">
      <span>Falls through to next case</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387185216" value="2">
      <span>Loop continues</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4387185216" value="3">
      <span>Program exits</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/java-comprehensive/mod-2.ipynb)

