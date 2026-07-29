class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Find rotting oranges
        Then add them for multisource BFS
        Traverse each minute
        Return time taken 
        '''

        rowCount = len(grid)
        colCount = len(grid[0])
        freshOranges = 0
        rottingOranges = deque()

        for row in range(rowCount):
            for col in range(colCount):
                if grid[row][col] == 1:
                    freshOranges += 1
                elif grid[row][col] == 2:
                    rottingOranges.append((row, col))
        
        rottingMins = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        while rottingOranges and freshOranges > 0:

            for _ in range(len(rottingOranges)):
                row, col = rottingOranges.popleft()
                for rowDelta, colDelta in directions:
                    newRow = row + rowDelta
                    newCol = col + colDelta
                    if 0 <= newRow < rowCount \
                    and 0 <= newCol < colCount \
                    and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        rottingOranges.append((newRow, newCol))
                        freshOranges -= 1
            
            rottingMins += 1

        return rottingMins if freshOranges == 0 else -1




        

                    


        