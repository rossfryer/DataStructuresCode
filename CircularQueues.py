class CircularQueue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.count += 1

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.count == self.max_size

    def size(self):
        """Return the number of items in the queue."""
        return self.count


# Example usage:
queue = CircularQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())  # Expected output: 1
print(queue.dequeue())  # Expected output: 1
print(queue.peek())  # Expected output: 2

queue.enqueue(4)  # Works fine, as we made space by dequeuing

# If you uncomment the following line, it will raise an error because the queue is full:
#queue.enqueue(5)
