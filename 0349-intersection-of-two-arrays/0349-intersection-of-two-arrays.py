class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = list(set(nums1))
        set2 = list(set(nums2))
        result = []
        for i in set1:
            if i in set2:
                result.append(i)
        return result
        