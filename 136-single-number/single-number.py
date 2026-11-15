class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        seen2 = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else :
                seen2.add(i)
        for i in seen :
            if i not in seen2:
                return i
        # print(seen)
        # print(seen2)