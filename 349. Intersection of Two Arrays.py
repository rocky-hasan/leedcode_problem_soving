class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1.sort()
        nums2.sort()
        res=[]
        res1=[]
        res2=[]
        for num in nums1:
            if num not in nums2:
                res1.append(num)
        res.append(res1)
        for num in nums2:
            if num not in nums1:
                res2.append(num)
        res.append(res2)
        return res
        

nums1 = [1,2,3]
nums2 = [2,4,6]
add=Solution()
r=add.findDifference(nums1,nums2)
print(r)