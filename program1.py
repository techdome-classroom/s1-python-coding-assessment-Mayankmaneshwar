class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        
        def dfs(grid, i, j):
           
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
         
            grid[i][j] = 'W'
            # Explore all 4 possible directions (up, down, left, right)
            dfs(grid, i-1, j)  # Up
            dfs(grid, i+1, j)  # Down
            dfs(grid, i, j-1)  # Left
            dfs(grid, i, j+1)  # Right
        
        num_islands = 0
       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L': 
                    dfs(grid, i, j)    
                    num_islands += 1  
        
        return num_islands

