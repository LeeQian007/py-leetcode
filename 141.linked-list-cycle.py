from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
