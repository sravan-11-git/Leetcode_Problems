class Solution:
    def reverse(self, x: int) -> int:
        min_32bit_signed = -2**31
        max_32bit_signed = 2**31 - 1

        if min_32bit_signed <= x <= max_32bit_signed:
            rev = 0
            sign = 1 if x >= 0 else -1
            x = abs(x)

            while x > 0:
                if rev > (max_32bit_signed - x % 10) // 10:
                    return 0  # Overflow check
                rev = rev * 10 + x % 10
                x = x // 10

            return sign * rev

        else:
            return 0
        