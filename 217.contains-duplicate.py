class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort / use HashSet
        # nlogn + 1  /  n + n
        check = set()

        for n in nums:
            if n in check:
                return True
            check.add(n)
        return False