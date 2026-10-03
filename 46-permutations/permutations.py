class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        curr = []
        ans = []

        def f():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for i in range(0,len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    f()
                    curr.pop()
        f()
        return ans