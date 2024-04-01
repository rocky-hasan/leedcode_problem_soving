


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        newnums=nums.sort()
        ln=len(set(nums))
        for i in range(ln):
            if nums[i]==target:
                return i
            else:
                return -1

nums = [4,5,6,7,0,1,2]
target = 0
c=Solution()
res=c.search(nums,target)
print(res)