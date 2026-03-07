class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        currSum = 0
        for num in nums:
            currSum += num
            prefix.append(currSum)

        print(prefix)
        seen = dict()
        count = 0
        for i in prefix:
            if i-k in seen:
                count+=seen[i-k]  ## Important!!
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

        return count