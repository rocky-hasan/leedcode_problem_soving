'''Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        empty_num=[]
        empty_num1=[]
        for  new_num in nums:
            
            if new_num == val:
                empty_num.append('_')
            else:
                empty_num1.append(new_num)
        empty_num1.extend(empty_num)  
        return empty_num1

nums = [3,2,2,3]
val = 3
obj=Solution()
result=obj.removeElement(nums,val)
print(result)





