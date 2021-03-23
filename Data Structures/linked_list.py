class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            # This loop ends on the last node where you have data and next
            while current.next:
                current = current.next
            current.next = node

    def insertAtBeginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtIndex(self, index, data):
        current = self.head
        curr_idx = 0
        node = Node(data)
        previous = current
        while current:
            if curr_idx == index:
                node.next = current.next
                previous.next = node
            previous = current
            current = current.next
            curr_idx += 1

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def display(self):
        current = self.head
        # This loop goes further than the last node and so the value is actually None here
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def findValueIndex(self, index):
        current = self.head
        curr_idx = 0

        if index < 0:
            return None

        while current:
            if curr_idx == index:
                return current.data
            curr_idx += 1
            current = current.next


ll = linked_list()

ll.insert(5)
ll.insert(2)
ll.insert(1)
ll.insert(7)
ll.insert(10)
ll.insert(15)


ll.display()

ll.insertAtBeginning(99)
ll.display()
print(ll.length())
print("Value at: {}".format(ll.findValueIndex(0)))

# Inserting at index 2
ll.insertAtIndex(2, 999)
ll.display()
