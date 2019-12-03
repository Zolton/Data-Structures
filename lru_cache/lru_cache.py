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
        self.limit = limit

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
        if self.cache.get(key, "gabba") != "gabba":
            # Step 1: Move to tail of list as most recently accessed
            # Record new location
            newest = self.node.move_to_end(self.cache[key])

            #Step 2 
            #???

            # Step 3: Profit! Add new key-value pair
            self.cache[key] = newest
            return self.cache[key].value

        # If there is no key, return None
        else:
            answer = self.cache.get(key, None)
            return answer

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

        # If key already exists, overwrite value in DLL
        if self.cache.get(key, "gabba") != "gabba":

            # Delete old value
            self.node.delete(self.cache[key])

            # Add new value to tail
            update = self.node.add_to_tail(value)

            # Update cache with new location
            self.cache[key] = update  

        # If key does not exist:
        elif self.cache.get(key, "gabba") == "gabba":

            # First check if there's room
            if len(self.cache) == self.limit:

                # If not:
                # Step 1: Find oldest node,
                # Store as the address, ie - 0x000001B7150EF3D0
                oldNode = self.node.head

                
                # Step 2: Find dictionary entry for oldNode:
                for i in self.cache.items():
                    # i[0] = key name, i[1] = node address
                    # Step 2a: If there's a match
                    if oldNode is i[1]:
                        # Step 2b: Record it
                        itemDel = i[0]

                # Step 3: Once out of the loop, delete the key
                self.cache.pop(itemDel)
                
                # Step 4: Remove it from the list
                self.node.remove_from_head()

                # Step 5: Send the key-value back through now that there's room
                self.set(key, value)

            # If there's room, add it in
            else:
                newValue = self.node.add_to_tail(value)
                self.cache[key] = newValue
                return value
            
        # If key already exists, overwrite value in DLL
        
        # Add key to cache
        # Add value to head of DLL, and update key with its node
        
