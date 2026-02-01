class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ptr1 = nums[0]
        n = sorted(nums[1:])
        print(n)
        return ptr1+n[0]+n[1]
