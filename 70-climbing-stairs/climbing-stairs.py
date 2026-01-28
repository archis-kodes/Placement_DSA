class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2 or n==3:
            return n
        count_map = [-1] * (n+1)
        count_map[0] = 0
        count_map[1] = 1
        count_map[2] = 2
        for i in range(3, n+1):
            count_map[i] = count_map[i-1] + count_map[i-2]
        return count_map[n]