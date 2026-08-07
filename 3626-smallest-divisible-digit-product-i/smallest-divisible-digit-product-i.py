class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            temp = n

            while temp:
                r = temp % 10
                product *= r
                temp //= 10

            if product % t == 0:
                return n

            n += 1