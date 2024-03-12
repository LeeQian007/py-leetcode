import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max-heap --> which one is the most frequent one
        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values() ]
        heapq.heapify(maxHeap)

        time = 0

        # A list-like sequence optimized for data accesses near its endpoints.
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                # Pop the smallest item off the heap, maintaining the heap invariant.
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft())
        return time

