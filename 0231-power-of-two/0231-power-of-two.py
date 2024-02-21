import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ''''while(n>=0):
            if n%2 != 0 and n != 1:
                return False
            n = n // 2
        return True'''
        if n <= 0:
            return False
        else:
            result = math.log(n) / math.log(2)
            if 2**int(result) == int(n):
                return True
        return False
                
        