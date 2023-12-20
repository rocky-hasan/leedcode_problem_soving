class Solution:
    def romanToInt(self, s: str) -> int:
        m={   
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            }
        
        ans=0
        for i in range(len(mm)):
            if i<(len(mm)-1) and m[mm[i]]< m[mm[i+1]]:
                ans -= m[mm[i]]
            else:
                ans += m[mm[i]]
        return ans

mm='LVIII'
obj=Solution()
result=obj.romanToInt(mm)
print(result)