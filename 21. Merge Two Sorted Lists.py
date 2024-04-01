class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Initialize a dummy node to simplify the code
        current = dummy = ListNode()
        
        # Traverse both linked lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # Move the current pointer forward
            current = current.next
        
        # Append the remaining elements of the non-empty list
        current.next = l1 if l1 else l2
        
        # Return the head of the merged linked list (excluding the dummy node)
        return dummy.next

#convert regular Python list to linked list
def createLinkedList(arr):
    current=dummy = ListNode()
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

#to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Input lists
list1 = [1, 2, 4]
list2 = [3, 4, 5]

# Convert input lists to linked lists
l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

# Merge two sorted linked lists
solution = Solution()
result = solution.mergeTwoLists(l1, l2)

# Print the merged linked list
printLinkedList(result)
