class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for row in grid:
            for i in range(n):
                temp = []
                for j in range(n):
                    temp.append(grid[j][i])
                if temp == row:
                    count+=1
        return count