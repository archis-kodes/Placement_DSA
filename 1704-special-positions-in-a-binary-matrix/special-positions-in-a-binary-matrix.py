class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def isSpecial (matrix, row, col):
            for i in range(len(matrix)):
                if i==row:
                    continue
                if matrix[i][col] == 1:
                    return False
            for j in range(len(matrix[0])):
                if j==col:
                    continue
                if matrix[row][j] == 1:
                    return False
            return True
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += isSpecial(mat, i, j)
        return count