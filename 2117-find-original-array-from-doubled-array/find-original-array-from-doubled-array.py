class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        memory = dict()
        for i in changed:
            if i not in memory:
                memory[i] = 1
            else:
                memory[i] += 1

        result = []

        for i in range(len(changed)):
            if memory[changed[i]] == 0:
                continue
            double = 2*changed[i]
            if double not in memory or memory[double] == 0:
                return []
            else:
                memory[2*changed[i]] -= 1
                memory[changed[i]] -= 1
            result.append(changed[i])
        return result