# Object-Oriented Programming

**Duration:** 15 min

## Overview

Object-Oriented Programming is a critical component of java-comprehensive that professionals encounter regularly in production systems.

## Core Concepts

Understanding Object-Oriented Programming requires grasping several interconnected ideas:

**Principle 1** - The foundational concept that everything else builds upon. This appears consistently across different implementations and contexts.

**Principle 2** - How theory translates into practical systems. This principle shapes architectural decisions at every scale.

**Principle 3** - The integration point where Object-Oriented Programming connects with other system components. Mastering this prevents common failures.

## Key Techniques

**Technique 1** - The standard approach used by most practitioners. Reliable, well-documented, appropriate for typical scenarios.

**Technique 2** - The high-performance variant used when standard approaches don't meet requirements. Requires deeper understanding but provides better results in constrained situations.

**Technique 3** - The robust variant that handles edge cases and degraded conditions. Essential for production systems that can't fail silently.

## Implementation Guide

Implementing Object-Oriented Programming effectively requires:

1. **Clear Requirements** - Understand exactly what you're trying to accomplish before starting
2. **Design Pattern Selection** - Choose an approach appropriate for your constraints
3. **Iterative Development** - Build incrementally, testing at each stage
4. **Comprehensive Testing** - Validate with realistic data before deployment
5. **Production Monitoring** - Observe behavior in the real environment

## Real-World Patterns

Professionals apply Object-Oriented Programming in diverse ways depending on context:

- **High-Throughput Systems** - Optimization strategies differ from real-time systems
- **Resource-Constrained Environments** - Techniques vary when hardware is limited
- **Distributed Systems** - Object-Oriented Programming behaves differently at scale
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

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

> **💡 Tip:** Best Practice: Use encapsulation to protect your data. Make fields private and provide public getter/setter methods.

> **💡 Tip:** Common Mistake: Forgetting to use @Override annotation when overriding methods. This helps catch errors at compile time.

Learn more: https://docs.oracle.com/javase/tutorial/java/concepts/

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is a class?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386907264" value="0">
      <span>An instance of an object</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386907264" value="1">
      <span>A blueprint for creating objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386907264" value="2">
      <span>A method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386907264" value="3">
      <span>A variable</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is inheritance?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386900992" value="0">
      <span>Creating multiple objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386900992" value="1">
      <span>A class inheriting from another class</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386900992" value="2">
      <span>Creating a method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386900992" value="3">
      <span>Declaring a variable</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What does encapsulation do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386858816" value="0">
      <span>Speeds up code</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386858816" value="1">
      <span>Protects data and controls access</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386858816" value="2">
      <span>Creates loops</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386858816" value="3">
      <span>Declares variables</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is polymorphism?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386856896" value="0">
      <span>Multiple objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386856896" value="1">
      <span>One interface, many forms</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386856896" value="2">
      <span>Creating classes</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386856896" value="3">
      <span>Declaring methods</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is the purpose of a constructor?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854592" value="0">
      <span>To destroy objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854592" value="1">
      <span>To initialize objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854592" value="2">
      <span>To create methods</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854592" value="3">
      <span>To declare variables</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What does the static keyword do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854272" value="0">
      <span>Makes code faster</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854272" value="1">
      <span>Creates instance variables</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854272" value="2">
      <span>Creates class-level members</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854272" value="3">
      <span>Declares methods</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is an interface?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386861888" value="0">
      <span>A class</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386861888" value="1">
      <span>A contract for classes to implement</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386861888" value="2">
      <span>A method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386861888" value="3">
      <span>A variable</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What is an abstract class?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386862784" value="0">
      <span>A regular class</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386862784" value="1">
      <span>A class that cannot be instantiated</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386862784" value="2">
      <span>A method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386862784" value="3">
      <span>An interface</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What does the this keyword refer to?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386857984" value="0">
      <span>The class</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386857984" value="1">
      <span>The current object</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386857984" value="2">
      <span>A method</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386857984" value="3">
      <span>A variable</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>

Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes. It's the foundation of Java and enables you to write modular, reusable, and maintainable code. OOP principles include encapsulation, inheritance, polymorphism, and abstraction. Understanding OOP is crucial for professional Java development and building large-scale applications.

```java title="ClassExample.java"
public class Car {
    private String brand;
    public Car(String brand) { this.brand = brand; }
    public void display() { System.out.println("Brand: " + brand); }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota");
        car.display();
    }
}
```



```
Brand: Toyota
```

```java title="Inheritance.java"
class Animal {
    void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking"); }
}
public class Test {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```
Eating
Barking
```

```java title="Polymorphism.java"
class Shape {
    void draw() { System.out.println("Shape"); }
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
class Rectangle extends Shape {
    @Override void draw() { System.out.println("Rectangle"); }
}
```

```
Polymorphism example
```

```java title="Encapsulation.java"
public class Person {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```
Encapsulation example
```

```java title="Constructor.java"
public class Student {
    private String name;
    public Student() { this.name = "Unknown"; }
    public Student(String name) { this.name = name; }
}
```

```
Constructor example
```

```java title="StaticExample.java"
public class Counter {
    static int count = 0;
    Counter() { count++; }
    static void display() { System.out.println("Count: " + count); }
}
public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter.display();
    }
}
```

```
Count: 2
```

```java title="Interface.java"
interface Animal {
    void sound();
}
class Dog implements Animal {
    public void sound() { System.out.println("Woof"); }
}
class Cat implements Animal {
    public void sound() { System.out.println("Meow"}; }
}
```

```
Interface example
```

```java title="AbstractClass.java"
abstract class Vehicle {
    abstract void start();
    void stop() { System.out.println("Stopped"); }
}
class Car extends Vehicle {
    void start() { System.out.println("Car started"); }
}
```

```
Abstract class example
```

```java title="ThisKeyword.java"
public class Example {
    int x = 10;
    void display() {
        int x = 20;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
    }
}
```

```
Local: 20
Instance: 10
```

```java title="SuperKeyword.java"
class Parent {
    void display() { System.out.println("Parent"); }
}
class Child extends Parent {
    void display() {
        super.display();
        System.out.println("Child");
    }
}
```

```
Parent
Child
```

```java title="FinalKeyword.java"
public class FinalExample {
    final int MAX = 100;
    final void display() { System.out.println("Final method"); }
}
final class ImmutableClass { }
```

```
Final keyword example
```

>
  <p class="font-semibold mb-3">❓ What does the super keyword do?</p>
  <div class="space-y-2">
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854656" value="0">
      <span>Calls parent class methods</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854656" value="1">
      <span>Creates objects</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854656" value="2">
      <span>Declares variables</span>
    </label>
    <label class="flex items-center gap-2 cursor-pointer">
      <input type="radio" name="q4386854656" value="3">
      <span>Creates loops</span>
    </label>
  </div>
  <button class="quiz-btn mt-3 px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700">Check Answer</button>
  <p class="quiz-result text-sm mt-2 hidden"></p>
</div>
## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/java-comprehensive/mod-3.ipynb)

