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
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue.enqueue(node)
        while self.queue.len() > 0:
            # If there's something in the queue, print it, then pop it.,
            # Then check if it has family. Just once!  
            # Got 10 mill?  Don't matter, we're in a loop, will
            # get to it eventually - just print/pop once
            current = self.queue.dequeue()
            print(current.value)
            # Got a left?  Add it in
            if current.left is not None:
                 self.queue.enqueue(current.left)
            # Got a right? add it in
            if current.right is not None:
                self.queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack.push(node)
        while self.stack.len() > 0:
            current = self.stack.pop()
            print(current.value)
            if current.left is not None:
                 self.stack.push(current.left)
            if current.right is not None:
                self.stack.push(current.right)
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # def pre_order_dft(self, node):



    # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass