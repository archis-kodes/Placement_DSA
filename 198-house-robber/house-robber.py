class Solution:
    def rob(self, nums: List[int]) -> int:
        cumulative_cash = [-1]*len(nums)

        def solve(idx):
            if idx>=len(nums):
                return 0
            if cumulative_cash[idx] !=-1:
                return cumulative_cash[idx]
            # Fill up
            a = nums[idx] + solve(idx+2) # Take
            b = solve(idx+1) # Not Take
            cumulative_cash[idx] = max(a, b)
            return cumulative_cash[idx]
        return solve(0)

