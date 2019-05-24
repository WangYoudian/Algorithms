class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0

        def DFS(grid, m, n, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == "0":
                return
            grid[i][j] = "0"

            DFS(grid, m, n, i - 1, j)
            DFS(grid, m, n, i, j - 1)
            DFS(grid, m, n, i + 1, j)
            DFS(grid, m, n, i, j + 1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    DFS(grid, m, n, i, j)
                    count += 1
                    
        return count