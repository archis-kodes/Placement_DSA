class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()
        for i in range(len(nums)):
            more = target - nums[i]
            if more in memory:
                return (memory[more], i)
            else:
                memory[nums[i]] = i
        return -1