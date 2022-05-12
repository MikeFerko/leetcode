'''
Linked List construction with push method, delete node method, and print the linked list method
'''

# Node class
class Node:
    # constructor for initializing the node object
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Constructor for initializing the head
    def __init__(self):
        self.head = None
    
    # function to insert a new node at the beginning of the LL
    def push(self, newValue):
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode
    
    # Given a reference to the head of the LL
    # and a position, delete the node at a given position
    def deleteNode(self, position):
        # if the LL is empty
        if self.head is None:
            return
        # if the position to remove a node is at the beginning of the LL
        if position == 0:
            self.head = self.head.next
        index = 0
        current = self.head
        previous = self.head
        temp = self.head # store head node
        while current is not None:
            if index == position:
                temp = current.next
                break
            previous = current
            current = current.next
            index += 1
        previous.next = temp
        return previous
    
    def printLL(self):
        temp = self.head
        while temp:
            if temp.next != None:
                print(" %d " % (temp.value),end="->")
            else:
                print(" %d " % (temp.value),end="-> NULL")
            temp = temp.next

if __name__=="__main__":
    # Driver program to test above function
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)

    print ("Created Linked List: ")
    llist.printLL()
    print("\n")
    llist.deleteNode(4)
    print ("\nLinked List after Deletion at position 4: ")
    llist.printLL()
    print("\n")