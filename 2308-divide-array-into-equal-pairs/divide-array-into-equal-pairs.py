class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        memory = dict()
        for num in nums:
            if num not in memory:
                memory[num] = 1
            else:
                memory[num] += 1
        for i in memory:
            if memory[i]%2!=0:
                return False
        return True