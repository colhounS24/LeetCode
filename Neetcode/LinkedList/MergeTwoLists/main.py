# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Both lists are already sorted, but they could have a different length.
        final_node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                final_node.val = list2.val
                final_node.next = list2.next
                list2 = list2.next
            elif list2.val > list1.val:
                final_node.val = list1.val
                final_node.next = list1.next
                list1 = list1.next
            else: # equal
                final_node.val = list1.val
                final_node.next = list1.next
                final_node = final_node.next

                final_node.val = list2.val
                final_node.next = list2.next
                list1 = list1.next
                list2 = list2.next
            
            final_node = final_node.next

        if list1 and not list2:
            while list1:
                final_node.val = list1.val
                final_node.next = list1.next

                final_node = final_node.next
                list1 = list1.next

        if list2 and not list1:
            while list2:
                final_node.val = list1.val
                final_node.next = list1.next

                final_node = final_node.next
                list2 = list2.next

        return final_node
