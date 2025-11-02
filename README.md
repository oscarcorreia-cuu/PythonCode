## Python code repository for BSE224 / DDA1101 Python Programming

### T3FlowControl.py
A simple Python script demonstrating **basic flow control**.  
It prints a greeting message and evaluates a simple comparison (`5 > 3`) to show how conditional expressions work.

### T3Conditional.py
A Python script illustrating **conditional statements and loops**.  
It includes commented examples of:
- `if` / `elif` / `else` conditions,
- `while` loops with counters,
- `for` loops with `break`,
- Iterating over strings and lists.

The script currently prints a message demonstrating the Python `for` statement.

### T4DataStructures.py — what it contains

A quick tour of Python **data structures** using small, readable examples. The file (mostly via commented snippets) shows:
- Creating and printing strings for student names.
- Building a **list** of students, looping with `for`, and common list ops: `append`, `insert`, `remove`, indexing, and slicing.
- A **set** example to illustrate automatic de-duplication.
- A working **dictionary** `my_dict = {"name": "Alice", "age": 25, "city": "New York"}` that is printed to the console.

### T5FunctionsIntroduction_Part1.py
Intro functions with three variants of “hello world”: prints directly, greets a named user, and returns a formatted greeting; then loops over a `students` list and prints each returned greeting. :contentReference[oaicite:0]{index=0}

### T5FunctionsIntroduction_Part2.py
Covers function parameters: a sum with a default argument, commented examples of `*args`, and two active `**kwargs` demos that print keys/values and compute totals (addition and multiplication). :contentReference[oaicite:1]{index=1}

### T5FunctionsIntroduction_Part3.py
Shows regular vs. lambda functions by implementing a `cube(x)` (with a print) and a lambda equivalent, calling both to display results. :contentReference[oaicite:2]{index=2}

### T5FunctionsIntroduction_Part4.py
Demonstrates single vs. multiple return values: `calculate1` returns a sum; `calculate2` returns (sum, difference), with examples of tuple unpacking and using the results. :contentReference[oaicite:3]{index=3}

### T5Module.py
A tiny utility module exporting two functions: `count_vowels(text)` and `reverse_string(text)`. :contentReference[oaicite:4]{index=4}

### T5Module_test.py
Imports the custom module and tests it by counting vowels and reversing a sample string, printing both results. :contentReference[oaicite:5]{index=5}

### T5RockPaperScissors.py
Interactive Rock–Paper–Scissors game: gets validated player input, random computer choice, determines and prints the winner; runs via `play_game()`. :contentReference[oaicite:6]{index=6}

### T5RockPaperScissors_Cheat.py
Variant of the game that reveals (prints) the computer’s choice before the player inputs theirs—useful for “cheating” or debugging flow—then proceeds as usual. :contentReference[oaicite:7]{index=7}

### T7Car.py
This module defines a `Car` class that simulates basic vehicle operations.
