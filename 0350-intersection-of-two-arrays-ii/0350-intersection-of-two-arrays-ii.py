class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        res = min(len(nums1),len(nums2))
        if len(nums1) <= len(nums2):
            copy1 = nums1.copy()
        else: 
            copy1 = nums2.copy()
        for i in range(res):
            if copy1[i] in nums1:
                if copy1[i] in nums2:
                    output.append(copy1[i])
                    if copy1 == nums1:
                        nums2.remove(copy1[i])
                    else:
                        nums1.remove(copy1[i])
        return output