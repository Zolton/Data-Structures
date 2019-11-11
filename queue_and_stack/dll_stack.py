
import sys
#sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self, node = None):
        self.size = 0
        self.node = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.node.add_to_head(value)

    def pop(self):
        self.node.remove_from_head()

    def len(self):
        return self.size
