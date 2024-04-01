'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Notice that the solution set must not contain duplicate triplets.'''
class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sorting the list is essential for the solution
        result = []
        n = len(nums)
        print(f'length: {n}')

        for i in range(n - 2):  # Loop until the third last element
            print(f'Here i : {i} nums[i]= {nums[i]} nums[i-1]= {nums[i-1]}')
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate  elements
            
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                print(f'Total : { nums[i]} + {nums[left]} + {nums[right]}= {total}')
                if total == 0:
                    print(f'append: {([nums[i], nums[left], nums[right]])}')
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Skip duplicate elements
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicate elements
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

nums = [-1, 0, 1, 2, -1, -4]
res = Solution()
print(res.threeSum(nums))
