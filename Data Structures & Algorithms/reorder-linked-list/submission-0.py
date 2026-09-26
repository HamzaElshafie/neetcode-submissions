# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the end of the first half
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # split into two lists 
        # for eg: 2 → 4 → 6 → 8 → 10
        # first list:   2 → 4 → 6 → None
        # second list:  8 → 10 → None
        second = slow.next
        slow.next = None

        # reverse second half
        # second list:  8 → 10 → None
        # second list:  10 → 8 → None
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # merge the two lists alternatively
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
