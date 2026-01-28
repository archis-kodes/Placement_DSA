class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        price_table = [-1]*len(cost)
        price_table[-1] = cost[-1]
        price_table[-2] = cost[-2]
        def solve(idx):
            if price_table[idx] != -1:
                return price_table[idx]
            price_table[idx] = cost[idx] + min(solve(idx+1), solve(idx+2))
            return price_table[idx]

        index0 = solve(0)
        index1 = solve(1)
        return min(index0, index1)