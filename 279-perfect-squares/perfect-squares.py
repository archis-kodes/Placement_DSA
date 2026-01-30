class Solution:
    def numSquares(self, n: int) -> int:
        def all_squares(n):
            temp = []
            i=1
            while i**2 <= n:
                temp.append(i**2)
                i+=1
            return temp

        min_sq_table = dict()
        def min_perfect_sq(n):
            
            # Base Condition
            if n==0:
                return 0
            
            # In Memo
            if n in min_sq_table:
                return min_sq_table[n]
            
            # Fresh Case
            all_sq = all_squares(n)
            temp = []
            for sq in all_sq:
                a = min_perfect_sq(n - sq) +1 # That number
                temp.append(a)
            min_sq_table[n] = min(temp)
            return min_sq_table[n]
        return min_perfect_sq(n) 