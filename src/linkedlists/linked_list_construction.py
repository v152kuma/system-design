# Linked List Construction
# Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None / null. The class should support:
#
# Setting the head and tail of the linked list.
# Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
# Removing given nodes and removing nodes with given values.
# Searching for nodes with given values.
# Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods all take in actual Nodes as input parameters—not integers (except for insertAtPosition, which also takes in an integer representing the position); this means that you don't need to create any new Nodes in these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario.
#
# If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language like Java or TypeScript to get a better idea of what each input parameter is.
#
# Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None / null.
#
# Sample Usage
# // Assume the following linked list has already been created:
#     1 <-> 2 <-> 3 <-> 4 <-> 5
#                             // Assume that we also have the following stand-alone nodes:
# 3, 3, 6
# setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
# setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
# insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
# insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
# insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
# removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
# remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
# containsNodeWithValue(5): true

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == node:
            return

        self.remove(nodeToInsert) #detach

        temp = self.head

        while temp is not None:

            if temp == node:
                nodeToInsert.next = temp
                nodeToInsert.prev = temp.prev
                if temp.prev:
                    temp.prev.next = nodeToInsert
                else:
                    self.head = nodeToInsert
                temp.prev = nodeToInsert
                break
            temp = temp.next



    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == node:
            return

        self.remove(nodeToInsert)

        temp = self.head
        while temp is not None:
            if temp == node:
                nodeToInsert.prev = temp
                nodeToInsert.next = temp.next

                if temp.next:
                    temp.next.prev = nodeToInsert
                else:
                    self.tail = nodeToInsert
                temp.next = nodeToInsert
                break
            temp = temp.next


    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        counter = 1
        temp = self.head
        while temp is not None:
            if counter == position:
                self.insertBefore(temp, nodeToInsert)
                return
            counter +=1
            temp = temp.next
        self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        temp = self.head
        while temp is not None:
            next_node = temp.next
            if temp.value == value:
                self.remove(temp)
            temp=next_node

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


    def containsNodeWithValue(self, value):
        # Write your code here.
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

