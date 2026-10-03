class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        curr = []
        ans = []

        def f(start):

            ans.append(curr.copy())

            for i in range(start,len(nums)):
                curr.append(nums[i])
                f(i+1)
                curr.pop()
        f(0)
        return ans