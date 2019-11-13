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
            #print("Current self value: ", self.value)
            #print("Going left with ", value)
            if self.left is None:
                # print("Went left, found None, gonna insert")
                # print("Current self.value: ", self.value)
                # print("Value to be inserted on the left: ", value)
                self.left = BinarySearchTree(value)
                #print("self.left.value is ", self.left.value)
                return
            else:
                #print("Current self value: ", self.value)
                #print("Went left, gonna continue")
                self = self.left
                return self.insert(value)
        if value >= self.value:
            #print("Current self value: ", self.value)
            #print("Going right with ", value)
            if self.right is None:
                # print("Went right, found None, gonna insert")
                # print("Current self.value: ", self.value)
                # print("Value to be inserted on the right: ", value)
                self.right = BinarySearchTree(value)
                #print("self.right.value is ", self.right.value)
                return
            else:
                #print("Current self value: ", self.value)
                #print("Went right, gonna continue")
                self = self.right
                return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        #To search a given key in Binary Search Tree, 
        # we first compare it with root, if the key is 
        # present at root, we return root. If key is greater 
        # than root’s key, we recur for right subtree of root node. 
        # Otherwise we recur for left subtree.
        if self.value is target:
            #print("success! We're done")
            return True
        if target > self.value:
            if self.right is None:
                #print("Nothing to the right, returning None")
                return False
            else:
                # print("Continuing down the right side")
                # print("target is: ", target)
                # print("current self.value: ", self.value)
                self = self.right
                #print("next to be searched: ", self.right.value)
                return self.contains(target)
        if target < self.value:
            if self.left is None:
                #print("Nothing to the left, returning None")
                return False
            else:
                #print("Continuing down the left side")
                #print("target is: ", target)
                #print("current self.value: ", self.value)
                self = self.left
                #print("next to be searched: ", self.left.value)
                return self.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until null, return value
        if self.right is None:
            return self.value
        else:
            self = self.right
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #Check every node, but only once
        # Go left until null, then go back and go right
        if self is None:
            return
        else:
            cb(self.value)
            # if self.left is not None:
            #left = self.left
            # if self.right is not None:
            #right = self.right
            #self = left
            if self.left is not None:

                self.left.for_each(cb)
            #self = right
            if self.right is not None:
                self.right.for_each(cb)
            
            
            #while self.right is not None:

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
