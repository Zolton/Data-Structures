import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self = self.left
                return self.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self = self.right
                return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value is target:
            return True
        if target > self.value:
            if self.right is None:
                return False
            else:
                self = self.right
                return self.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                self = self.left
                return self.contains(target)
        
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            self = self.right
            return self.get_max()

    def for_each(self, cb):
        if self is None:
            return
        else:
            cb(self.value)
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #print(self.stack.pop())
        
        
        if node.left is not None:
            #print("left value, ", node.left.value)
            self.in_order_print(node.left)
        print("+", node.value)
        if node.right is not None:
            #print("right value, ", node.right.value)
            self.in_order_print(node.right)
        
        
        #print("value, ", node.value)
        
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        #while node.left is not None:
        #     print(node.value)
        #     self.bft_print(node.left)
        # #while node.right is not None:
        #     print(node.value)
        #     self.bft_print(node.right)
        # while node.left is not None or node.right is not None:
        #     for i in node:
        #         print(node.left, nod)
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    #def dft_print(self, node):
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # def pre_order_dft(self, node):



    # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass