class Queue:
    def __init__(self, maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.size = 0
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return False
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.items[self.rear] = item
            self.size += 1
            return True

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return False
        else:
            item = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return item

    def isFull(self):
        return self.size == self.maxSize

    def isEmpty(self):
        return self.size == 0

    def printQueue(self):
        print(self.items)

