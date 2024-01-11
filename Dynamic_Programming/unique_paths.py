def uniquePaths(self, m: int, n: int) -> int:

    grid = [[0 for i in range(n)] for j in range(m)]  # Initalises the arrays to form our grid

    for col_num, col in enumerate(grid):
        for row_num, _ in enumerate(col):
            # Base case for the origin as there can be a 1 x 1 square
            if row_num == col_num == 0:
                grid[col_num][row_num] = 1
            # These two are base cases for the two squares next to the grid[0][0] thats done in here to account for other edge cases
            elif col_num == 1 and row_num == 0:
                grid[col_num][row_num] = 1
            elif row_num == 1 and col_num == 0:
                grid[col_num][row_num] = 1
            # These two next if statements are for the edges where they can only be reached by one other square
            elif row_num == 0:
                grid[col_num][row_num] = 1
            elif col_num == 0:
                grid[col_num][row_num] = 1
            # Otherwise add the addition of the two squares that can go to the current square
            else: 
                grid[col_num][row_num] = grid[col_num - 1][row_num] + grid[col_num][row_num - 1]

    # Finally return the last cell as that will contain all our paths
    return grid[m - 1][n - 1]