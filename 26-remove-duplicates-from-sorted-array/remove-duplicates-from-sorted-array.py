class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = []
        for i in nums[:]:
            if i not in new:
                new.append(i)
            else:
                nums.remove(i)
        print (nums)