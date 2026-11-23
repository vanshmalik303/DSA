class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans = 0
        for i in nums:
            while i!=maxi:
                i+=1
                ans+=1
        return ans

                