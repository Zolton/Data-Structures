from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10, node=None):
        self.length = 1 if node is not None else 0
        self.node = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Cache holds the key/node location of value, 
        # DLL holds the actual value
        # When retrieved, 
        # remove from current location, and add_to_tail,
        # then update hash table with new key/location

        # If the key exists
        if self.cache[key] is True:
            # Add value to tail/most recently accessed
            newest = self.node.add_to_tail(self.cache[key].value)

            # Update location in cache
            self.cache[key] = newest

            #removes value from old location
            self.node.delete(self.cache[key].value)

            # Return requested value
            return self.cache[key].value
            
        # If there is no key, return None
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if limit > 10, remove entry #11 
        # and send everything back through again
        if len(self.cache) > 10:
            self.node.remove_from_head()
            self.set(key, value)

        # If key doesn't exist, create it
        if self.get(key) == None:
            newValue = self.node.add_to_tail(value)
            self.cache[key] = newValue
            return value

        # If key already exists, overwrite value in DLL
        else:
            # Delete old value
            self.node.delete(self.cache[key])
            # Add new value to tail
            update = self.node.add_to_tail(value)
            # Update cache with new location
            self.cache[key] = update
        
