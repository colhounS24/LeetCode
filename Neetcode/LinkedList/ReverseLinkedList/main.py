"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # step through the list, for each node swap the value and store next in a temp variable
        # A -> B -> C == C-> B -> A
        prev = None
        curr = head 
        while True:
            if curr:
                temp_next = curr.next # pointer to the next node
                curr.next = prev # set the pointer to the previous address
                prev = curr
                curr = temp_next
                
            else:
                break

        return prev

        