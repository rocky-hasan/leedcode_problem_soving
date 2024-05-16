class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        a=k%n
        print(a)
        print(nums[:-a])
        print(nums[-a:])
        nums[:]=nums[-a:]+nums[:-a]
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
res=Solution()
r=res.rotate(nums,k)
print(r)
# output=[5,6,7,1,2,3,4]