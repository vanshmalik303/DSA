class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2 != 0:
            return 0

        k = (total + target) // 2
        n = len(nums)

        dp = [[-1] * (k + 1) for _ in range(n)]

        def solve(i, target):
            if i == 0:
                if target == 0 and nums[0] == 0:
                    return 2
                if target == 0 or nums[0] == target:
                    return 1
                return 0

            if dp[i][target] != -1:
                return dp[i][target]

            notPick = solve(i-1, target)

            pick = 0
            if nums[i] <= target:
                pick = solve(i-1, target-nums[i])

            dp[i][target] = pick + notPick
            return dp[i][target]

        return solve(n-1, k)