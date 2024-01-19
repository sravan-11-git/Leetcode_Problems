import math
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 1
        if n%2 == 0:
            count += 1
            twos = (n//2)
            for i in range(twos-1,0,-1):
                ones = n - (i*2)
                total = ones + i
                denominator = math.factorial(ones)*math.factorial(i)
                probability = math.factorial(total)//(denominator)
                count = probability + count
        else:
            twos = (n//2)
            for i in range(twos,0,-1):
                ones = n - (i*2)
                total = ones + i
                denominator = math.factorial(ones)*math.factorial(i)
                probability = math.factorial(total)//(denominator)
                count = probability + count
        return count



            


        