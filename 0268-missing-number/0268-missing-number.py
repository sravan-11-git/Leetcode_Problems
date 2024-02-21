class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        n = len(nums)
        old = (n*(n+1)//2) - 1
        result = old - sum1
        return result + 1
        