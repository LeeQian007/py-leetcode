class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return self.intersection(set1, set2) if len(set1) > len(set2) else self.intersection(set2, set1)

    def intersection(self, set1, set2):
        return [x for x in set2 if x in set1]

nums1 = [1,2,2,1]
nums2 = [2,2]

Solution.intersection()