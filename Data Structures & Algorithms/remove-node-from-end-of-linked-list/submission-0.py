# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # move second ptr `n` nodes away from first
        for _ in range(n+1):
            second = second.next
        
        # reach end of list
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next

# We can traverse the linked list keeping track of an index and once we reach index == n, we save the node we will delete's next and then make the prev node's next point to the save next, so we bypass the node we want to delete

# but since this is a single linked list, we always need to keep track of the prev node so we can do that

# acc we cant do this because we are removing the nth node from the end of the list not from front

# but we can do a two pointer solution where one pointer starts at the beginning and then the other starts `n` nodes apart and then we keep going until the second pointer becomes None, then that means we are standing at the node we want to delete with the first pointer and then we can simply do the deletion like in my previous solution