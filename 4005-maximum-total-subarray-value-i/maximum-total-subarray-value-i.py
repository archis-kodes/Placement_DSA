class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)
        return k*(maximum-minimum)