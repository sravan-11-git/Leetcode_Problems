import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            result = math.log(n) / math.log(2)
            if 2**int(result) == int(n):
                return True
        return False

                
        