'''Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pos=1
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i-1] !=nums[i]:
                nums[pos]=nums[i]
                pos+=1
        return pos

nums= [0,0,1,1,1,2,2,3,3,4]
rs=Solution()
res=rs.removeDuplicates(nums)
print(res)

