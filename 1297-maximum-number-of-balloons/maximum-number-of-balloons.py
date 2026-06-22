class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = 0
        a = 0
        l = 0
        o = 0
        n = 0
        for i in text:
            if i=='b':
                b+=1
            elif i == 'a':
                a += 1
            elif i == 'l':
                l += 1
            elif i == 'o':
                o += 1
            elif i == 'n':
                n += 1
        o = o//2
        l = l//2
        return min(b, a, l, o, n)