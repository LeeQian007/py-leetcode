# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev, slow = slow, nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

