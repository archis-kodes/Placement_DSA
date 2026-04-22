class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            res = 0
            while n:
                digit = n%10
                res = res*10 + digit
                n=n//10
            return res
        return abs(n-reverse(n))