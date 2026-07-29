class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rowCount = len(grid)
        colCount = len(grid[0])
        maxAreaCount = 0
        visited = set()
        queue = deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        for row in range(rowCount):
            for col in range(colCount):
                currentAreaCount = 0

                if (row, col) not in visited \
                and grid[row][col] == 1:
                    currentAreaCount += 1
                    visited.add((row, col))
                    queue.append((row, col))
                
                while queue:
                    currRow, currCol = queue.popleft()
                    for rowDelta, colDelta in directions:
                        newRow = currRow + rowDelta
                        newCol = currCol + colDelta
                        if 0 <= newRow < rowCount \
                        and 0 <= newCol < colCount \
                        and (newRow, newCol) not in visited \
                        and grid[newRow][newCol] == 1:
                            currentAreaCount += 1
                            visited.add((newRow, newCol))
                            queue.append((newRow, newCol))
                
                maxAreaCount = max(maxAreaCount, currentAreaCount)

        return maxAreaCount

                    
