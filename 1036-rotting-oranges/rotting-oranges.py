from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isFresh(grid, i, j):
            if i<0 or i>=len(grid):
                return False
            elif j<0 or j>=len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            return False

        rotten = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])

        if fresh==0:
            return 0

        duration = 0

        while rotten:
            n = len(rotten)
            while(n):
                i, j = rotten.popleft()
                n-=1

                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dir_i, dir_j in dirs:
                    if isFresh(grid, i+dir_i, j+dir_j):
                        grid[i+dir_i][j+dir_j] = 2           # Rotten
                        rotten.append([i+dir_i, j+dir_j])
                        fresh -=1
            duration +=1

        if fresh == 0:
            return duration - 1
        return -1