class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        events = dict()
        for start, end in requests:
            if start not in events:
                events[start] = 1
            else:
                events[start] += 1
            if end+1 not in events:
                events[end+1] = -1
            else:
                events[end+1] += -1

        events = dict(sorted(events.items()))

        result = []
        cumSum = 0
        for i in range(len(nums)):
            if i in events:
                cumSum += events[i]
            result.append(cumSum)
        
        result.sort()
        nums.sort()

        summed = 0
        for i in range(len(nums)):
            summed += nums[i]*result[i]
            summed = summed % MOD
        return summed