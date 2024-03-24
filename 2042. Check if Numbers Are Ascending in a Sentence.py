'''Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
Output: true
Explanation: The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.'''
class Solution:

    def areNumbersAscending(self, s: str) -> bool:
        new_s=s.split(' ')
        empt=[]
        for st in new_s:
            empt.append(st)
        x=len(empt)
        max_num=-1
        new_empt=[]
        for i in range(x):
            if empt[i].isdigit():
                
                new_empt.append(int(empt[i])) 
            else:
                pass
        # here check every number thats is big or not
        for st in new_empt:
            if st>max_num:
                max_num=st
            else:
                return False
        return True

s = "1 box has 7 blue 4 red 6 green and 12 yellow marbles"
res=Solution()
p=res.areNumbersAscending(s)
print(p)