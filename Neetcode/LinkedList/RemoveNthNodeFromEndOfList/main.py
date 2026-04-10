# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Firstly reverae the list
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        rev_list = prev

        # keep counting until I get to n-1, then set n-1.next to curr.next.next
        idx = 0
        curr = rev_list
        while curr:

            if n == 1:
                rev_list = rev_list.next
                break

            if idx == n - 2:
                # Now we want to skip the nth node
                curr.next = curr.next.next
            idx += 1
            curr = curr.next

        # Reverse again and return the list
        prev = None
        curr = rev_list

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        return prev