from queueDef import *


newQueue = Queue(10)
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)

newQueue.printQueue()
newQueue.dequeue()
newQueue.printQueue()
item = newQueue.dequeue()
newQueue.printQueue()
print(item)
