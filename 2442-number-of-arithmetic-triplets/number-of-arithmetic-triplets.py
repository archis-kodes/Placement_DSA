class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        memory = set(nums)
        count = 0
        for num in nums:
            if num+diff in memory and num+diff+diff in memory:
                count+=1

        return count