class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        count = 0

        while a >= b:
            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1

            a -= temp
            count += multiple

        if negative:
            count = -count

        return count