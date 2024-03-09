from typing import List


class Solution:
    @staticmethod
    def findUnsortedSubarray(nums: List[int]) -> int:

        n = len(nums)
        maxN, right = float("-inf"), -1
        minN, left = float("inf"), -1

        for i in range(n):
            if nums[i] < maxN:
                right = i
            else:
                maxN = nums[i]

            if nums[n - 1 - i] > minN:
                left = n - i - 1
            else:
                minN = nums[n - 1 - i]


        return 0 if left == -1 else right - left + 1


nums = [2,6,4,8,10,9,15]
Solution.findUnsortedSubarray(nums)
