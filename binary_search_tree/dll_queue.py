import sys
#sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
#test = new DoublyLinkedList


class Queue:
    def __init__(self, node=None):
        self.size = 1 if node is not None else 0
        self.node = DoublyLinkedList()
        self.node.tail = node
        # Why is our DLL a good choice to store our elements?
            # Need access to head and tail
        # self.storage = ?

    def enqueue(self, value):
        print("working queue", value)
        self.size += 1
        self.node.add_to_head(value)
        

    def dequeue(self):
        print("working")
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.node.remove_from_tail()
        #print("value is ", self.node.tail)
        

    def len(self):
        return self.size
