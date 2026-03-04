class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def findIslands(grid, i, j):

            # Range Condition Check
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return

            # Base Condition
            if grid[i][j] == "0":
                return

            # Mark Visited
            grid[i][j] = "0"

            # Traverse
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dir_i, dir_j in dirs:
                new_i, new_j = i+dir_i, j+dir_j
                findIslands(grid, new_i, new_j)

            return True

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if findIslands(grid, i, j):
                        count+=1
        return count