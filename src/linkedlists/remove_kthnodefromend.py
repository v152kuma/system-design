# Remove Kth Node From End
# Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.
#
# The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).
#
# Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer.
#
# Note that your function doesn't need to return anything.
#
# You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.
#
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
#
# Sample Input
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
# k = 4
# Sample Output
# // No output required.
# // The 4th node from the end of the list (the node with value 6) is removed.
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_kth_node_from_end(head, k):

    fast_pointer = head
    slow_pointer = head

    for i in range(k):
        fast_pointer = fast_pointer.next

    if fast_pointer is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while fast_pointer.next is not None:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next

    slow_pointer.next = slow_pointer.next.next

def remove_kth_node_using_len(head, k):
    current = head
    length = 0

    while current is not None:
        length += 1
        current = current.next

    if length == k:
        head.value = head.next.value
        head.next = head.next.next
        return

    current = head
    for i in range(length - k - 1):
        current = current.next

    current.next = current.next.next