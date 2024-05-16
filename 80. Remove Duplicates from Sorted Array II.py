class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
                
        return pos
   
nums = [1, 1, 1, 2, 2, 3]
df = Solution()
new_length = df.removeDuplicates(nums)
print(new_length)  # Expected output: 5
print(nums[:new_length])  # Expected modified array: [1, 1, 2, 2, 3]

