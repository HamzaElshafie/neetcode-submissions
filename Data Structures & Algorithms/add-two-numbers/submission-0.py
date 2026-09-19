# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            first_digit = l1.val if l1 else 0
            second_digit = l2.val if l2 else 0

            curr_sum = first_digit + second_digit + carry
            digit = curr_sum % 10
            carry = curr_sum // 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
        


# 6 -> 2 -> 6
# 4 -> 5 -> 6
# ___________
# 0 -> 8 -> 2

# We need to handle carry overs

# Ok so what i am thinking its acc really good that the numbers are stored in reverse because this is how we would acc do the sums if we were to do them by hand. Also this will help us deal with carry overs

# So what we can do is traverse the linked lists at the same time, inspecting the same positions respectively. So in the eg. add the the value at the nodes 1 and 4. If the value exceeds 10, we store the rightmost digit at the new linkedlist as a node and we take the carry over to the next step

# we keep doing so until we reach the end of the lists (I am assuming both lists will have same length for now to be honest)