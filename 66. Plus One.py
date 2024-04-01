'''You are given a large integer represented as an integer array digits,
 where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result=0
        empty=[]
        for char in digits:
            result=result*10+char
        newres= result+1

        while newres>0:
            empty.insert(0,newres%10)
            newres//=10
        return empty



digits=[1,2,3]
obj=Solution()
result=obj.plusOne(digits)
print(result)



