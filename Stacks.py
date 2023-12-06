class Stack:
    def __init__(self):
        self.items = [] # This makes a dynamic stack. How would you make a static stack?

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.items.pop() # Python command removes last item from a list and returnes it.

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.items[-1] #Python allows you to look at the last item in the list using [-1]

    def printStack(self):
        print(self.items)

stackTest = Stack()
stackTest.push('gaspard')
stackTest.push('thomas')
stackTest.push('Mr.Fryer')
stackTest.printStack()
popped = stackTest.pop()
print(popped)
popped = stackTest.pop()
print(stackTest.peek())
popped = stackTest.pop()
print(popped)
popped = stackTest.pop()
print(popped)





