class Solution:
    def reverse(self, x: int) -> int:
        y=0
        if x<0:
            y=int(str(x)[1:][::-1])*-1
            
        else:
            y=int(str(x)[::-1])
            
        if y > 2 ** 31 - 1 or y < -2 ** 31:
            return 0
        return y
        

res=Solution()
n=res.reverse(-123)
print(n)