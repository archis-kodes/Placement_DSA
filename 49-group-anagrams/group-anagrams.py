class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = {}
        for i in strs:
            idx = "".join(sorted(i))
            if idx not in memory:
                memory[idx] = [i]
            else:
                memory[idx].append(i)
        
        result = []
        for key, value in memory.items():
            result.append(value)
        return result