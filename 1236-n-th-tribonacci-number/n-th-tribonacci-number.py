class Solution:
    def tribonacci(self, n: int) -> int:
        count_map = dict()
        count_map[0] = 0
        count_map[1] = 1
        count_map[2] = 1
        def tri(n):
            if n in count_map:
                return count_map[n]
            count_map[n] = tri(n-1) + tri(n-2) + tri(n-3)
            return count_map[n]
        return tri(n)