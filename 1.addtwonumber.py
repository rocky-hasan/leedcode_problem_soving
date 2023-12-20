class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

nums=[1,2,3,4,5,6]
target=6
obj=Solution()
result=obj.twoSum(nums,target)
print(result)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         return next((i, j) for i, x in enumerate(nums) for j, y in enumerate(nums[i+1:], i+1) if x + y == target)


