
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
       
        def ms(nums):
            if len(nums)<=1:
                return nums

            mid = len(nums)//2

            left = ms(nums[:mid])
            right = ms(nums[mid:])

            result = []
            i = 0
            j = 0
            while i <len(left) and j<len(right):
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            # if left:
            #     result.append(left[i])
            #     i+=1
            # if right :
            #     result.append(right[j])
            #     j+=1
            result.extend(left[i:])
            result.extend(right[j:])


            return result
        return ms(nums)