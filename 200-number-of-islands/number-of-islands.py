class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Check each unvisited cell and increment the total count of islands if a new land is found.
        Add all the connecting lands as visited 
        '''

        row_count = len(grid)
        col_count = len(grid[0])
        visited = set()
        total_island_count = 0
        queue = deque()

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for row in range(row_count):
            for col in range(col_count):
                if (row, col) not in visited \
                and grid[row][col] == "1":
                    total_island_count += 1
                    queue.append((row, col))
                    visited.add((row, col))

                    while queue:
                        current_row, current_col = queue.popleft()
                        for row_delta, col_delta in directions:
                            new_row = current_row + row_delta
                            new_col = current_col + col_delta

                            if 0 <= new_row < row_count \
                            and 0 <= new_col < col_count \
                            and (new_row, new_col) not in visited \
                            and grid[new_row][new_col] == "1":
                                queue.append((new_row, new_col))
                                visited.add((new_row, new_col))
        
        return total_island_count





        
        