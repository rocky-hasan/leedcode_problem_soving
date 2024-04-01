'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring
 consisting of non-space characters only.
 Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split(' ')
        print(s)
        newstring=s[-1].strip()
        return len(newstring)
        

# string_name="Hello World"
# string_name="   fly me   to   the moon  "
string_name="luffy is still joyboy"
obj=Solution()
result=obj.lengthOfLastWord(string_name)
print(result)