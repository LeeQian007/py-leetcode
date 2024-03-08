class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):

            for j in dp.copy():
                if nums[i] + j == target:
                    return True
                dp.add(nums[i] + j)

        return True if target in dp else False