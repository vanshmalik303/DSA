class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0 
        x2 = x
        while x>0:
            r = x%10
            reverse = reverse * 10 + r
            x = x//10
        return reverse == x2