class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        temp=x
        rev=0
        while temp!=0:
            digit = temp % 10
            rev=rev * 10 + digit
            temp //= 10
        return rev==x
            



x=int(input("Enter a integer number"))
obj=Solution()
result=obj.isPalindrome(x)
print(result)
