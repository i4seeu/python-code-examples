# lets implement queue and stack data structures in python
class Stack:
    """A simple stack implementation using a list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack. 
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
class Queue:
    """A simple queue implementation using a list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue. 
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """Return the item at the front of the queue without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
if __name__ == "__main__":
    # Example usage of Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack size:", stack.size())  # Output: Stack size: 3
    print("Stack top item:", stack.peek())  # Output: Stack top item: 3
    print("Popped item from stack:", stack.pop())  # Output: Popped item from stack: 3
    print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

    # Example usage of Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue size:", queue.size())  # Output: Queue size: 3
    print("Queue front item:", queue.front())  # Output: Queue front item: 1
    print("Dequeued item from queue:", queue.dequeue())  # Output: Dequeued item from queue: 1
    print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2