class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans