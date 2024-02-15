'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.'''

# head = [1,1,2]
# new_head=set(head)
# print(list(new_head))

# Definition for singly-linked list...
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head





