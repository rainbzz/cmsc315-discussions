"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
            # List = stack storage; end of list = top of stack
            self.items = []

    def push(self, value):
        # Add to the end of the list = top of stack: LIFO
        self.items.append(value)

    def pop(self):
        # Removes/returns the top item. Checking is_empty() first avoids
        # an IndexError from calling list.pop() on an empty list
        if self.is_empty():
            print("Stack is empty! Nothing to pop.")
            return None
        return self.items.pop()

    def peek(self):
        # Returns the top item w/o removing it. It'll useful when needed
        # Also can check what's on top before deciding to pop it
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.items[-1]

    def is_empty(self):
        return not self.items


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        # Adds to the back and keeps existing items in order
        # Since new items wait behind older one: FIFO
        self.items.append(value)

    def dequeue(self):
        # Removes/returns the front item. Difference between this and
        # the top is the distinction between LIFO and FIFO, same idea but
        # different structure. pop() = same end (top) /// dequeue() = opposite end (front)
        if self.is_empty():
            print("Queue is empty! Nothing tp dequeue.")
            return None
        return self.items.popleft()

    def front(self):
        # Same as before it removes/returns front item. Difference between
        # peek() and front() is the same as front vs top.
        # peek() =  newest item; pop() would remove
        # front() = oldest item; dequeue() would remove
        if self.is_empty():
            print("Queue is empty! Nothing at the front.")
            return None
        return self.items[0]

    def is_empty(self):
        return not self.items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    stack = Stack()

    # push 4 values
    print("Pushing 'plate 1', 'plate 2', 'plate 3', 'plate 4' onto the stack")
    stack.push("plate 1")
    stack.push("plate 2")
    stack.push("plate 3")
    stack.push("plate 4")
    print(f"Current stack (bottom > top): {stack.items}")

    # LIFO check:
    print(f"\nPeeking at the top of the stack: {stack.peek()}")
    print("Popping from the stack one at a time (LIFO order):")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}")

    # Edge case: pop on empty
    print("\nStack is now empty. Trying to pop again:")
    stack.pop()

    # Edge case: peek on empty
    print("Trying to peek at the empty stack:")
    stack.peek()

    # Edge case: single item > remove > confirm
    print("\nSingle-item stack test:")
    single_stack = Stack()
    single_stack.push("only plate")
    print(f"  Stack before removal: {single_stack.items}")
    removed = single_stack.pop()
    print(f" Removed: {removed}")
    print(f" Is the stack empty? {single_stack.is_empty()}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    # Enqueue 4 values
    print("Enqueuing 'customer 1', 'customer 2', 'customer 3', 'customer 4'...")
    queue.enqueue("customer 1")
    queue.enqueue("customer 2")
    queue.enqueue("customer 3")
    queue.enqueue("customer 4")
    print(f"Current queue (front -> back): {list(queue.items)}")

    # FIFO check:
    print(f"\nChecking who's at the front: {queue.front()}")
    print("Dequeue one at a time (FIFO order):")
    while not queue.is_empty():
        print(f"  Served: {queue.dequeue()}")

    # Edge case: dequeue on empty
    print("\nQueue is now empty. Trying to dequeue again:")
    queue.dequeue()

    # Edge case: front on empty
    print("Trying to check the front of the empty queue:")
    queue.front()

    # Edge case: single item > remove > confirm
    print("\nSingle-item queue test:")
    single_queue = Queue()
    single_queue.enqueue("only customer")
    print(f"  Queue before removal: {list(single_queue.items)}")
    removed = single_queue.dequeue()
    print(f"  Removed: {removed}")
    print(f"  Is the queue empty now? {single_queue.is_empty()}")

## # # # # # # # # # # ##
## REAL WORLD SCENARIO ##
## # # # # # # # # # # ##
# Stack use case: text editor undo

    print("\n=== REAL-WORLD SCENARIO: TEXT EDITOR UNDO (Stack) ===")
    undo_stack = Stack()
    edits = ["Typed 'Hello'", "Typed ' World'", "Deleted 'World'", "Typed ' Python'"]
    for edit in edits:
        print(f"Action performed: {edit}")
        undo_stack.push(edit)

    print("\nUser presses Ctrl+Z (Undo) three times:")
    for _ in range(3):
        print(f"  Undoing: {undo_stack.pop()}")

# Queue use case: printer job queue

    print("\n=== REAL-WORLD SCENARIO: PRINTER JOB QUEUE (Queue) ===")
    print_queue = Queue()
    documents = ["Resume.pdf", "Essay.docx", "Photo.png", "Invoice.pdf"]
    for doc in documents:
        print(f"Sent to printer: {doc}")
        print_queue.enqueue(doc)

    print("\nPrinter processes jobs in the order they were received:")
    while not print_queue.is_empty():
        print(f"  Printing: {print_queue.dequeue()}")

if __name__ == "__main__":
    main()
