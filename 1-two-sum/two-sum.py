class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)-1):
            req = target - nums[left]
            for right in range(left+1, len(nums)):
                if nums[right] == req:
                    return [left, right]