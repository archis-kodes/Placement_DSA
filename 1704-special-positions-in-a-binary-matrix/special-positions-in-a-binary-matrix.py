class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def isSpecial (matrix, row, col):
            rowSum = sum(matrix[row])
            colSum = sum(r[col] for r in matrix)
            return rowSum==1 and colSum==1
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += isSpecial(mat, i, j)
        return count