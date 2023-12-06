class Collection:
    def __init__(self):
        self.items = []       # Internal structure
        self.index = 0        # Internal pointer for iteration

    def addItem(self, data):
        """Adds a data item to the collection."""
        self.items.append(data)

    def resetNext(self):
        """Resets the internal pointer to the start of the collection."""
        self.index = 0

    def hasNext(self):
        """Returns True if there is another item to retrieve."""
        return self.index < len(self.items)

    def getNext(self):
        """
        Retrieves the next item from the collection.
        Raises IndexError if no more items.
        """
        if self.hasNext():
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise IndexError("No more items in the collection")

    def isEmpty(self):
        """Returns True if the collection is empty."""
        return len(self.items) == 0


STUFF = Collection()
STUFF.addItem(12)
STUFF.addItem(3)
STUFF.addItem(5)
STUFF.addItem(7)
STUFF.addItem(9)
STUFF.addItem(11)
STUFF.resetNext()

while STUFF.hasNext():
    ITEM = STUFF.getNext()
    print(ITEM)

