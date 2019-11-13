import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        #Go left if 
        #Go right if 
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #To search a given key in Binary Search Tree, 
        # we first compare it with root, if the key is 
        # present at root, we return root. If key is greater 
        # than root’s key, we recur for right subtree of root node. 
        # Otherwise we recur for left subtree.
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until null, return value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #Check every node, but only once
        # Go left until null, then go back and go right
        pass

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
