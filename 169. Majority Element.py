from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major={}
        majority=0
        ans=0
        for num in nums:
            major[num]=major.get(num,0)+1

        for k,v in major.items():
            if v>majority:
                majority=v
                ans=k
        return ans
            


            
nums = [2,2,1,1,1,2,2,3,5,5,5,5,5,5]
res=Solution()
print(res.majorityElement(nums))

