class Stacks:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.popped = self.items.pop()
            return self.popped

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1]

stackTest = Stacks()
stackTest.push('archie')
stackTest.push('owen')
stackTest.push('Mr.Fryer')
print(stackTest)
popped = stackTest.pop()
print(popped)
popped = stackTest.pop()
print(stackTest.peek())
popped = stackTest.pop()
print(popped)
popped = stackTest.pop()
print(popped)





