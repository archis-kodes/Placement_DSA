class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def generate(words):
            array = [0]*26
            result = []
            # Frequency Maintain
            for i in words:
                array[ord(i) - ord('a')] += 1
            # Join
            for i in range(26):
                if array[i]!=0:
                    result.append(chr(97+i)*array[i])
            return "".join(result)

        memory = dict()
        for i in strs:
            sorted_i = generate(i)
            if sorted_i not in memory:
                memory[sorted_i] = [i]
            else:
                memory[sorted_i].append(i)
        result = []
        for key, values in memory.items():
            result.append(values)
        return result