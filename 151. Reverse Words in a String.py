class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split()
        news=s[::-1]
        result=' '.join(news)
        return result

s = "the sky is blue"
# Output: "blue is sky the"
res=Solution()
print(res.reverseWords(s))