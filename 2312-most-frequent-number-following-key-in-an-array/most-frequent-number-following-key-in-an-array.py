class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count_map = dict()
        max_freq = 0
        max_freq_element = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in count_map:
                    count_map[nums[i+1]] = 1
                else:
                    count_map[nums[i+1]] += 1
                if count_map[nums[i+1]] > max_freq:
                    max_freq = count_map[nums[i+1]]
                    max_freq_element = nums[i+1]

        return max_freq_element