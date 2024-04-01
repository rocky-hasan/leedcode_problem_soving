'''Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult=int(num1)*int(num2)
        return str(mult)

num1 = "2"
num2 = "3"
c=Solution()
res=c.multiply(num1,num2)
print(res)