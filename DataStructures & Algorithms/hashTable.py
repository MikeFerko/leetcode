from typing import List


# Node data structure - essentially a LinkedList node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table with separate chaining
class HashTable:
    def __init__(self, capacity = 50):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity
    
    def hash(self, key: str) -> int:
        hashSum = 0
        for id in range(0, len(key)):
            char = key[id]
            unicodeChar = ord(char)
            hashSum += (id + len(key))**unicodeChar
            hashSum = hashSum % self.capacity
        return hashSum
    
    def insert(self, key: str, value: List[str]) -> None:
        # increment the size
        self.size += 1

        # compute the index of the key
        index = self.hash(key)

        # go to the node corresponding to the hash
        node = self.table[index]

        if node is None:
            # create the node, add it, return it
            self.table[index] = Node(key, value)
            return
        
        # Collision. Iterate to the dn of the linked list at the provided index
        previous = node
        while node is not None:
            previous = node
            node = node.next
        
        # add a new node at the end of the list with the provided key/vlaue pair
        previous.next = Node(key, value)
    
    def search(self, key: str) -> None:
        # compute the hash
        index = self.hash(key)

        # go to the first node in the list in the table
        node = self.table[index]

        # Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        
        # Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value
    
    def delete(self, key: str) -> None:
        # Compute the hash
        index = self.hash(key)
        node = self.table[index]
        previous = None

        # Iterate to the requested node
        while node is not None and node.key != key:
            previous = node
            node = next
        
        # Now, node is either the requested node or none
        if node is None:
            # key not found
            return None
        else:
            # key was found
            self.size -= 1
            result = node.value

            # delete this element in the linked list
            if previous is None:
                node = None
            else:
                previous.next = previous.next.next
            
            # return the deleted result
            return result

    def display(self) -> None:
        n = len(self.table)
        for i in range(0, n):
            if self.table[i] is not None:

                print(f"Node {i}: [key: {self.table[i].key}, value: {self.table[i].value}]")


# Create a new HashTable
ht = HashTable(capacity=1000)

# Create some data to be stored
phone_numbers = ["555-555-5555", "444-444-4444"]

# Insert our data under the key "phoneDirectory"
ht.insert("phoneDirectory", phone_numbers)

# rest the variable for phone numbers
phone_numbers = None

# Retrieve the data we stored in the HashTable
phone_numbers = ht.search("phoneDirectory")

ht.display()
# find() retrieved our list object

# phone_numbers is now equal to ["555-555-5555", "444-444-4444"]