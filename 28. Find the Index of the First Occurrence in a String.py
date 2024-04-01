'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
 or -1 if needle is not part of haystack.

 Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1
        n=len(needle)
        hn=len(haystack)

        for i in range((hn-(n))+1):
            if haystack[i:i+n]==needle:
                return i
        else:
            return -1

haystack = "dfhdursadofsad"
needle = "sad"
obj=Solution()
result=obj.strStr(haystack,needle)
print('output:',result)