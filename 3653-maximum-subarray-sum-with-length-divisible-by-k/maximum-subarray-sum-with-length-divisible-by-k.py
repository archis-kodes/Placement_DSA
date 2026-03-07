class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        prefix = [0]
        currSum = 0
        for num in nums:
            currSum += num
            prefix.append(currSum)

        maxSubarraySum = prefix[k]
        for i in range(k):   # How many times loop will run
            subSum = 0
            for j in range(i,len(nums)-k+1, k):
                chunk = prefix[j+k] - prefix[j]

                # Kadane's Algorithm
                subSum = max(chunk, subSum + chunk)
                maxSubarraySum = max(subSum, maxSubarraySum)

        return maxSubarraySum