class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class double_linked_list:
    def __init__(self):
        self.head = None
