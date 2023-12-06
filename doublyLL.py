class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    # -------------------------
    # Insert at beginning
    # -------------------------
    def insert_beginning(self, data):

        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node


    # -------------------------
    # Insert at end
    # -------------------------
    def insert_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current


    # -------------------------
    # Delete a value
    # -------------------------
    def delete(self, value):

        current = self.head

        while current:

            if current.data == value:

                # Node is head
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev

                return

            current = current.next


    # -------------------------
    # Forward traversal
    # -------------------------
    def print_forward(self):

        current = self.head

        while current:
            print(current.data, end=" ⇄ ")
            current = current.next

        print("None")


    # -------------------------
    # Backward traversal
    # -------------------------
    def print_backward(self):

        current = self.head

        if current is None:
            return

        while current.next:
            current = current.next

        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev

        print("None")

dll = DoublyLinkedList()

dll.insert_beginning(30)
dll.insert_beginning(10)
dll.insert_end(40)
dll.insert_end(50)

print("Forward Traversal")
dll.print_forward()

print("Backward Traversal")
dll.print_backward()

print("Deleting 40")
dll.delete(40)

dll.print_forward()