# ================================ Optimal =========================================
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return - 1
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nc][nr] = 2
                        queue.append((nr,nc))
                        fresh -= 1
                minutes += 1
        return minutes if fresh == 0 else - 1
        