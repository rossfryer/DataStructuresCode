from linkedList import Node

class Stack:

    def __init__(self):
        self.top = None


    def isEmpty(self):
        return self.top is None


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None

        removed = self.top.data
        self.top = self.top.next
        return removed


    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data


    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.pop())
print("Top item:", s.peek())

s.display()