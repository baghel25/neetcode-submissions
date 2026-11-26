class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
         return 0
        row_ln = len(grid)
        col_in = len(grid[0])

        visited = set()
        land = 0 
        def dfs(row,col):
            queqe = collections.deque()
            queqe.append((row,col))
            visited.add((row,col))
            dir = [[0,1],[1,0],[-1,0],[0,-1]]

            while queqe:
                row_k,col_k = queqe.popleft()
                for dr,dc in dir:

                    new_row = dr+row_k
                    new_col = dc+col_k
                    if (0 <= new_row < row_ln
                    and 0 <= new_col < col_in 
                    and grid[new_row][new_col] == "1" 
                    and (new_row,new_col) not in visited 
                    ):
                        queqe.append((new_row,new_col))
                        visited.add((new_row,new_col))






        for r in range(row_ln):
            for c in range(col_in):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    land+=1

        
        return land
                    

                
