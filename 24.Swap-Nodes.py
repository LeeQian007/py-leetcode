from typing import Optional


class ListNode:
    pass


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair
        return dummy.next

