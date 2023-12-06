from linkedList import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None


    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:   # queue is empty
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:   # queue became empty
            self.rear = None

        return removed


    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data


    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

q = Queue()

q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")

q.display()

print("Dequeued:", q.dequeue())
print("Front item:", q.peek())

q.display()