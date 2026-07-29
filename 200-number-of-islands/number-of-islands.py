class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Check if new islands are found
        If so increment the total island count

        Mark all connected land as visited
        '''

        rowCount = len(grid)
        colCount = len(grid[0])
        visited = set()
        totalIsland = 0
        queue = deque()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        for row in range(rowCount):
            for col in range(colCount):
                if (row, col) not in visited \
                and grid[row][col] == "1":
                    totalIsland += 1
                    visited.add((row, col))
                    queue.append((row, col))
                
                while queue:
                    currentR, currentC = queue.popleft()
                    for dr, dc in directions:
                        newRow = currentR + dr
                        newCol = currentC + dc
                        if 0 <= newRow < rowCount \
                        and 0 <= newCol < colCount \
                        and (newRow, newCol) not in visited \
                        and grid[newRow][newCol] == "1":
                            visited.add((newRow, newCol))
                            queue.append((newRow, newCol))
            
        return totalIsland

            

        