class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_count = 0
        l_count = 0
        n = len(moves)

        for i in range(n):
            if moves[i] == 'L':
                l_count += 1
            elif moves[i] == 'R':
                r_count += 1
        return n - 2*min(l_count, r_count)