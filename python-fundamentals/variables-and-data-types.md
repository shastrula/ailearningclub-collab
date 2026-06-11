# Variables and Data Types

**Duration:** 15 min

## Core Principles

Understanding variables and data types is fundamental to Python programming. Variables are containers for storing data values, while data types define what kind of data can be stored.

Python is dynamically typed, meaning you don't explicitly declare variable types—Python infers them from the assigned value. This flexibility makes Python beginner-friendly while remaining powerful for production code.

## Key Concepts

**Variables:** Named references to data in memory. Use descriptive names following snake_case convention.

**Data Types:** Categories of data (int, float, str, bool, list, dict, tuple, set). Each has different operations and behaviors.

**Type Inference:** Python automatically determines type based on value. You can check with `type()` function.

## Essential Concepts

**Concept 1: Creating Variables** - Simply assign a value: `name = "Alice"`, `age = 25`. No declaration needed.

**Concept 2: Common Data Types**
- `int`: Whole numbers (42, -3, 0)
- `float`: Decimal numbers (3.14, -0.5)
- `str`: Text ("hello", 'world')
- `bool`: True/False values
- `list`: Ordered collections [1, 2, 3]
- `dict`: Key-value pairs {"name": "Bob", "age": 30}

**Concept 3: Type Conversion** - Convert between types with `int()`, `float()`, `str()`, etc.

## Practical Implementation

Here's how professionals work with variables and data types:

1. Use descriptive variable names that explain purpose
2. Understand type conversions to prevent bugs
3. Know which operations work with which types
4. Use appropriate data structures for your data

### Common Patterns

```python
# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

# Type checking
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>

# Type conversion
age_str = str(age)     # "25"
count = int("42")      # 42

# Collections
numbers = [1, 2, 3, 4, 5]
person = {"name": "Bob", "age": 30, "city": "NYC"}
```

## Real-World Example

A data analyst receives temperature data as strings: "72.5", "68.3", "75.1". They need to:
1. Convert to floats for calculations
2. Store in a list for analysis
3. Track measurement units in metadata

Understanding data types prevents silent errors where string comparisons ("75.1" > "72.5" = False!) give wrong results.

## Common Challenges

Practitioners often encounter:
- Type confusion causing unexpected behavior
- Forgetting to convert user input from strings
- Mixing incompatible types in operations
- Not understanding mutable vs immutable types

Recognizing these patterns helps avoid repeating them.

## Best Practices

- Use clear, descriptive variable names
- Understand your data type before operating on it
- Convert explicitly rather than relying on implicit conversions
- Use `type()` and `isinstance()` for debugging
- Document expected types in function signatures

## Practice Exercises

Try these in your Colab notebook:

1. Create variables of each data type
2. Check their types with `type()`
3. Perform type conversions
4. Create a list and dictionary with real data
5. Predict what happens when mixing types

## Next Steps

After mastering variables and data types, you'll be ready for:
- Operators and expressions
- Control flow (if/else statements)
- Working with data structures
