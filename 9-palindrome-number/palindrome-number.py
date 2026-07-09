class Solution:
    def isPalindrome(self, x: int) -> bool:
        n1 = x
        n2 = x
        count = 0
        digit = 1
        total = 0
        while n1>0:
            count+=1
            n1//=10
        while x>0:
            r = x%10
            total += r*(10**(count-digit))
            digit+=1
            x=x//10
        return(n2==total)