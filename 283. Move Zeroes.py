'''
Given an integer array nums, move all 0's 
to the end of it while maintaining the relative 
order of the non-zero elements.
Note that::: you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        newnums=[]
        for i in nums:
            if i!=0:
                newnums.append(i)
            
        zero_count=len(nums)-len(newnums)
        newnums.extend([0]*zero_count)
        print(newnums)
        
nums = [0,1,0,3,12]
result=Solution()
result.moveZeroes(nums)

