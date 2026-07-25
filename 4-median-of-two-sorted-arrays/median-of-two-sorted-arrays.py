class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        n,m = len(nums1),len(nums2)
        new = []
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1

        while i<n:
            new.append(nums1[i])
            i+=1
        while j<m:
            new.append(nums2[j])
            j+=1

        if len(new)%2==0:
            mid = len(new)//2
            ans = (new[mid]+new[mid-1])/2
            
        else:
            mid = len(new)//2
            ans = (new[mid])
        return (ans)