# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment helped shift my understanding of how Python lists work. I recognized that insert() and pop() don't just
add or remove values instantly; they physically shift every subsequent element in memory. This was familiar coming from JavaScript,
where array methods like splice() and unshift() behave the same way under the hood. I also practiced using conditional expressions
and boolean short-circuiting (like x or y) to write more concise functions while still validating inputs safely.

2. What challenges did you encounter, and how did you overcome them?
The main challenge was handling edge cases without crashing the program, for example, deleting from an invalid index or an empty list.
I overcame this by validating the index range before calling pop() and testing each function against unusual inputs early,
rather than assuming they'd "just work."

3. How do list operations impact performance in real-world applications?
This connects directly to real-world performance: inserting or deleting at the end of a list is fast (O(1)),
but doing so at the beginning or middle is slower (O(n)) because of the shifting involved. In applications like playlists, databases,
or queues, choosing the right operation and position can meaningfully affect speed at scale.