"""
Problems:
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

def create_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

l1 = create_linked_list([2, 4, 3])  # 表示数字342
l2 = create_linked_list([5, 6, 4])  # 表示数字465

# 计算两个链表表示的数字之和
solution = Solution1()
result = solution.addTwoNumbers(l1, l2)

# 打印结果链表
print_linked_list(result)  # 输出 7 -> 0 -> 8 -> None，表示数字807
