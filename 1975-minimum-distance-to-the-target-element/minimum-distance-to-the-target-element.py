class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = []
        for i in range(start, len(nums)):
            if nums[i] == target:
                res.append(abs(i-start))
                break
        
        for i in range(start+1):
            if nums[start-i] == target:
                res.append(abs(i))
                break
        
        return min(res)