class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        tup = []
        for i in range(len(nums)):
            tup.append((nums[i], i))
        tup = sorted(tup)
        
        win = []
        abs_count = 1000

        for i in range(len(tup)-2):
            if tup[i][0] == tup[i+1][0] == tup[i+2][0]:
                a = abs(tup[i][1] - tup[i+1][1]) + abs(tup[i+1][1] - tup[i+2][1]) + abs(tup[i+2][1] - tup[i][1])
                abs_count = min(a, abs_count)
        return abs_count if abs_count!=1000 else -1