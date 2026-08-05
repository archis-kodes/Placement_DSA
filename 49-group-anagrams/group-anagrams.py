class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = dict()
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in memory:
                memory[sorted_i] = [i]
            else:
                memory[sorted_i].append(i)
        result = []
        for key, values in memory.items():
            result.append(values)
        return result