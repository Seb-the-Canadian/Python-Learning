# Python Quick-Reference Toolbox

## 1. Core Concepts
- **Variables:** `name = "Ada"`, `age = 32`
- **Data Types:** `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`
- **Type Checking:** `type(value)`
- **Comments:** `# single-line`, `"""multi-line"""`

## 2. Strings
- **Concatenation:** `"Hello, " + name`
- **f-string:** `f"{name} is {age}."`
- **Methods:** `name.upper()`, `phrase.lower()`, `text.split()`, `" - ".join(list_var)`
- **Length:** `len(string)`

## 3. Numbers & Math
- **Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Math Functions:** `abs(x)`, `round(x, 2)`
- **Importing Math:** `import math`, then `math.sqrt(x)`, `math.pi`

## 4. Lists
- **Create:** `skills = ["Markdown", "Python"]`
- **Indexing:** `skills[0]`, `skills[-1]`
- **Slice:** `skills[1:3]`
- **Methods:** `skills.append("Meditation")`, `skills.pop()`, `skills.sort()`
- **Length:** `len(skills)`

## 5. Tuples vs Sets vs Dicts
- **Tuple (immutable list):** `coords = (10, 20)`
- **Set (unique items):** `unique_vals = {1, 2, 3}`
- **Dict (key/value):** `person = {"name": "Ada", "role": "Engineer"}`
- **Dict Access:** `person["name"]`, `person.get("role", "Unknown")`

## 6. Conditionals
    if condition:
        ...
    elif other_condition:
        ...
    else:
        ...
- Comparisons: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

## 7. Loops
### For Loop
    for item in collection:
        ...
### While Loop
    while condition:
        ...
- Use `break` to exit early, `continue` to skip to next iteration.
- Enumerate: `for index, value in enumerate(list_var):`

## 8. Functions
    def greet(name="friend"):
        return f"Hello, {name}!"
- Use docstring for clarity:
    def add(a: int, b: int) -> int:
        """Return the sum of two integers."""
        return a + b

## 9. Input & Output
- **Input:** `user_name = input("Name: ")`
- **Print:** `print("Result:", result)`
- **Formatted Print:** `print(f"{name} scored {score}/10")`

## 10. Common Utilities
- **Range:** `range(5)` → `0..4`, `range(start, stop, step)`
- **Zip:** `for name, pages in zip(books, page_counts):`
- **List Comprehension:** `[x * 2 for x in numbers if x > 0]`
- **Unpacking:** `a, b = pair`

## 11. Errors & Debugging
- Read the full error message.
- Use `print()` to inspect values.
- Test in small pieces (comment/uncomment code blocks).

## 12. Recommended Practice Pattern
1. Write a comment describing the goal.
2. Draft variables and sample data.
3. Build a loop or function to process data.
4. Print intermediate results.
5. Summarize in a final printout.

Keep this file open as a cheat sheet while you code. Update it whenever you learn a new pattern or trick!