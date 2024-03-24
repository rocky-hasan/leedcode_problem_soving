# Given the head of a singly linked list, reverse the list, and return the reversed list.
# list=[1,2,3,4,5]
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list=None
        current=head
        while current:
            next_node=current.next 
            current.next=new_list
            new_list=current
            current=next_node
        return new_list
# Create instances of ListNode for each value
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Link the nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

# Create a Solution instance
s = Solution()

# Reverse the linked list by passing the head node
reversed_head = s.reverseList(node1)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next