class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        preMax = nums[0]
        preMin = nums[0]

        for n in nums[1:]:
            curMax = max(n * preMax, n * preMin, n)
            curMin = min(n * preMax, n * preMin, n)
            preMax = curMax
            preMin = curMin
            res = max(curMax, res)
        return res