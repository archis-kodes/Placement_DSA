class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        memory = dict()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp = i - j
                if temp not in memory:
                    memory[temp] = [mat[i][j]]
                else:
                    memory[temp].append(mat[i][j])
        for i in memory.keys():
            memory[i] = sorted(memory[i], reverse = True)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                target = i - j 
                mat[i][j] = memory[target][-1]
                memory[target].pop()
        return mat