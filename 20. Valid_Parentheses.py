'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''
class Solution:
    def isValid(self, s: str) -> bool:
        #this is empty stack which follow LIFO
        stack=[]
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for prnths in s:
            if prnths in pairs:
                stack.append(prnths)
            elif len(stack)==0 or  prnths !=pairs[stack.pop()] :
                return False
        return len(stack) == 0
s="([]){}"
c=Solution()
print(c.isValid(s))
# pairs = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }
# if ')' in pairs:
#     print('Valid')
# else:
#     print('Invalid')
# print(pairs)