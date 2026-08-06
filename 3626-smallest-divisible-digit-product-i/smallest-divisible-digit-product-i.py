class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        def generateProduct(n):
            product = 1
            while (n):
                digit = n%10
                n = n//10
                product *= digit
            return product

        for i in range(11):
            product = generateProduct(num+i)
            remainder = product%t
            if remainder==0:
                return num+i