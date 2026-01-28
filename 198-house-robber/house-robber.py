class Solution:
    def rob(self, nums: List[int]) -> int:
        # cumulative_cash = [-1]*len(nums)
        # def solve(idx):
        #     if idx>=len(nums):
        #         return 0
        #     if cumulative_cash[idx] !=-1:
        #         return cumulative_cash[idx]
        #     # Fill up
        #     a = nums[idx] + solve(idx+2) # Take
        #     b = solve(idx+1) # Not Take
        #     cumulative_cash[idx] = max(a, b)
        #     return cumulative_cash[idx]
        # return solve(0)

        ### TABULATION
        table = [-1]*(len(nums)+1)
        table[0] = 0
        table[1] = nums[0]
        for i in range(2, len(nums)+1):
            steal = nums[i-1] + table[i-2] # Cant take profit till previous (i-1) house 
            skip = table [i-1]
            table[i] = max(steal, skip)
        return table[-1]