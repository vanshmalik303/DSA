class Solution:
    def reverse(self, x: int) -> int:
        if x<0 :
            sign = -1
        else:
            sign = 1
        number = str(abs(x))
        number = int(number[::-1])
        number = number*sign
        if (number<(-2)**31) or (number>(2)**31-1):
            return 0
        else:
            return number

