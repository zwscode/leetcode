# https://leetcode.com/problems/lru-cache/description/
# medium

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""

class LinkedNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Double linked list + hash table
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.__evict(key)
        self.__addToEnd(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.__delete(key)

        node = LinkedNode(key, value)
        self.cache[key] = node
        self.__addToEnd(node)
        
        if len(self.cache) > self.capacity:
            self.__delete(self.head.next.key)
    
    def __evict(self, key) -> LinkedNode: 
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def __delete(self, key) -> None:
        deleteNode = self.__evict(key)
        del deleteNode
        del self.cache[key]

    def __addToEnd(self, node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# OrderedDict + hash table
class LRUCache:
    def __init__(self, capacity: int):
        import collections
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # popitem(last=False) is FIFO, popitem(last=True) is LIFO
            self.cache.popitem(False)