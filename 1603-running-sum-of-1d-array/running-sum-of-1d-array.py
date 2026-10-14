class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        result = 0
        for i in nums:
        
            result += i
            ans.append(result)

            
        return ans