# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        newlist=sorted(nums1+nums2)
        ln=len(newlist)
        if ln%2==1:
            return newlist[ln//2]
        else:
            middle1=newlist[ln//2-1]
            middile2=newlist[ln//2]
            return float((middle1+middile2)/2)
 

nums1=[0,0]
nums2=[0,0]
obj=Solution()
result=obj.findMedianSortedArrays(nums1,nums2)
print(result)
