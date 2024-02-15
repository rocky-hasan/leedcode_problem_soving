class Solution:
    def search(self,nums: list[int], target: int) -> int:
        v=sorted(nums)
        left=0
        right=len(v)-1
        while left<=right:
            mid = left + (right - left) // 2
            if v[mid] == target:
                return mid
            elif v[mid]<target:
                left=mid+1
            else:
                right=mid-1
        else:
            return -1



nums = [-1,0,3,5,9,12]
target = 12
result=Solution()
res=result.search(nums,target)
print(res)