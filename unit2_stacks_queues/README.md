# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment helped me understand how Stack (LIFO) and Queue (FIFO) structures work under the hood, rather than just knowing their definitions.
Implementing push/pop/peek and enqueue/dequeue/front from scratch made the difference between "last in, first out" and "first in, first out" concrete—especially seeing 
how a stack's pop() and a queue's dequeue() remove from opposite ends relative to insertion, even though peek() and front() serve the same conceptual purpose (previewing the next item without removing it).

2. What challenges did you encounter, and how did you overcome them?
My biggest challenge was a runtime AttributeError on self.items. After tracing the traceback, I found a duplicate, incorrectly nested def __init__ inside Stack.__init__,
which silently prevented self.items from ever being created. Debugging it taught me to read indentation carefully and trust tracebacks to point to the real failure point.

3. Explain the differences between stacks and queues as this relates to real-world applications.
In real-world terms, stacks fit "undo" actions in software, where the most recent change should be reversed first, while queues model fairness-based ordering,
like a printer processing jobs in the order they were submitted or people waiting in a checkout line.


