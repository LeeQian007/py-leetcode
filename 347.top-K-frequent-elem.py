from typing import List


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # nlogn
        # count = {}  # { 1: 3 times }
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        #
        # sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
        # top_k = sorted_count[:k]
        #
        # top_keys = [key for key, _ in top_k]
        # return top_keys
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



nums = [1,1,1,2,2,3]

Solution.topKFrequent(nums,2)