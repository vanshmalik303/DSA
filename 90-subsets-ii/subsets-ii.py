class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        curr = []
        ans = []
        nums.sort()
        def f(sub):
            ans.append(curr.copy())

            for i in range(sub,len(nums)):
                if i > sub and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                f(i+1)
                curr.pop()
        f(0)
        return ans