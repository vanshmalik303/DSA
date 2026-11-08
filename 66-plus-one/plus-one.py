class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        num = int("".join(map(str,digits)))
        num+=1
        arr = list(map(int,str(num)))
        return arr