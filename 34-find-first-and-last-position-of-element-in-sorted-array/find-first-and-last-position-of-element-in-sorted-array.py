class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                left = mid
                right = mid

                while left > 0 and nums[left - 1] == target:
                    left -= 1

                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1

                return [left, right]

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return [-1, -1]