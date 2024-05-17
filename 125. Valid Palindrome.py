class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=s.lower()
        result=[]
        for i in new_s:
            if i.isalnum():
                result.append(i)
        print(result)
        filter_res=''.join(result)
        print(filter_res)
        return filter_res == filter_res[::-1]
        
s = "A man, a plan, a canal: Panama"
res=Solution()
ans=res.isPalindrome(s)
print(ans)