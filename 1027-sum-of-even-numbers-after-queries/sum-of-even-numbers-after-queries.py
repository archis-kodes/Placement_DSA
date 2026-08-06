class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Calcu;ate even sum
        even_sum = 0
        for i in nums:
            if i%2==0:
                even_sum += i
        result = []
        for query in queries:
            idx = query[1]
            val = query[0]
            if nums[idx]%2==0:  # Even
                even_sum -= nums[idx] # Remove
            nums[idx] += val
            if nums[idx]%2 == 0: # Even
                even_sum += nums[idx]
            result.append(even_sum)
        return result