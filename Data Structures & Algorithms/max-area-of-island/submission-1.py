class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # print(grid)
        if not grid:
            return 0 

        row_len = len(grid)
        col_len = len(grid[0])
        land = 0 
        visited = set()

        def dfs(row , col):
            mac = 1 
            queue = collections.deque()
            queue.append((row,col))
            visited.add((row,col))

            dir = [[0,1],[1,0],[-1,0],[0,-1]]
            while queue:
                row_,col_ = queue.popleft()

                for dr,dc in dir:
                    new_r = dr+row_
                    new_c = dc + col_

                    if(0<= new_r < row_len 
                    and 0<= new_c< col_len 
                    and grid[new_r][new_c] == 1
                    and (new_r,new_c) not in visited
                    ):
                       visited.add((new_r,new_c))
                       queue.append((new_r,new_c))
                       mac +=1

            return mac




        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and (r,c) not in visited:
                    
                    cu = dfs(r,c)
                    land = max(land,cu)


        return land

