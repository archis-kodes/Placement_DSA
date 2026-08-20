class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = dict()
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        freq_map = sorted(freq_map.items(), key=lambda item: item[1])
        new_map = dict()
        for i in freq_map:
            if i[1] not in new_map:
                new_map[i[1]] = [i[0]]
            else:
                new_map[i[1]].append(i[0])
        for i in new_map:
            new_map[i].sort(reverse = True)
                
        result = []
        for i in new_map:
            for j in new_map[i]:
                result += [j]*i
        return result