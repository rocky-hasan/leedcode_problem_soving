'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring
 consisting of non-space characters only.'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        found_word = False

        for char in reversed(s):
            if char.isalpha():
                found_word = True
                length += 1
            elif found_word:
                break

        return length
        

string_name=input('enter a string: \n')
obj=Solution()
result=obj.lengthOfLastWord(string_name)
print(result)