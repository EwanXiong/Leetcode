"""
two non-null linked lists that represent two non-negative integers. They store each digit in reverse order, and each node can only store one digit number.
Please add the two numbers and return a linked list of the sum in the same form.
You can assume that neither of these numbers begins with a zero except for the number 0.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
