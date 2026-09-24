
class Stack:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data):
        node = self.Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_not_empty(self):
        return not (self.top is None)