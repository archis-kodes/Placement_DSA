class Solution:
    def validPalindrome(self, s: str) -> bool:
        life = 1
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                sl = s[left+1:right+1]
                sr = s[left:right]
                return (sl == sl[::-1]
                or sr == sr[::-1])
            left+=1
            right-=1
        return True