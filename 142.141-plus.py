from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while True:
            if not (fast and fast.next):return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break

        slow = head
        if slow != fast:
            slow, fast = slow.next, fast.next
        return slow

