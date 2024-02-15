# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        v=sorted(strs)
        fisrt=v[0]
        last=v[-1]
        emp=""
        for i in range(min(len(fisrt),len(last))):
            if (fisrt[i] !=last[i]):
                return emp
            emp +=fisrt[i]
        return emp
strs=["fl","fluuu","floo"]
sol=Solution()
result=sol.longestCommonPrefix(strs) 
print(result)