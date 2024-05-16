class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:]=nums1[:m]
        
        nums2[:]=nums2[:n]
        
        nums1.extend(nums2)
        nums1.sort()
        return sorted(nums1)
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#Output: [1,2,2,3,5,6]
res=Solution()
new=res.merge(nums1,m,nums2,n)
print((new))