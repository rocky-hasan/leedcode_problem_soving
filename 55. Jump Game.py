class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        step=0
        for i in range(n):
            if i>step:
                return False 
            step=max(step,i+nums[i])
            if step>=n-1:
                return True
        return True
            
nums = [2, 3, 1, 1, 4]
# nums=[3, 2, 1, 0, 4]
res=Solution()
ans=res.canJump(nums)
print(ans)