class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        flip = False
        memory = dict()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                target = i+j
                if target not in memory:
                    memory[target] = [mat[i][j]]
                else:
                    memory[target].append(mat[i][j])
        result = []
        for key, value in memory.items():
            if key%2 == 0:
                result += value[::-1]
            else:
                result+=value
        return result
