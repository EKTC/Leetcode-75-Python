# =========== Solution 1 ========== #
# We create a helper function to recurse on 
# Our condition is that its next to a cell that is the same colour as it
# We continue checking cells till all the relevant cells have been checked
#
# The cell_check function has 5 variables:
# @ image -> the grid that allows us to update elements when conditions are satisfied
# @ colour_shift -> this is the colour we want to shift to if the conditions are met
# @ match_colour -> This is the colour we want to check if they are the same 
# @ row_index -> The current row index of the cell
# @ column_index -> The current column index of the cell
def floodFill(image, sr, sc, color):
    
    def cell_check(image, colour_shift, match_colour, row_index, column_index):
        # Two sets of if statements broken up to be a bit more readable
        # First IF is checking if the indicies of the cell is a valid one
        # Second IF is checking if we have already shifted a cell or its not the same colour
        # We need to have this as it sort of acts the same as a visited array
        # Wherein we dont revisit cells that have already been checked as that would allow for an infinite loop
        if row_index > len(image) - 1 or column_index > len(image[0]) - 1  or row_index < 0 or column_index < 0:
            return
        if image[row_index][column_index] == colour_shift or image[row_index][column_index] != match_colour:
            return

        if image[row_index][column_index] == match_colour:
            image[row_index][column_index] = colour_shift
            
            cell_check(image, colour_shift, match_colour, row_index - 1, column_index)
            cell_check(image, colour_shift, match_colour, row_index, column_index - 1)
            cell_check(image, colour_shift, match_colour, row_index + 1, column_index)
            cell_check(image, colour_shift, match_colour, row_index, column_index + 1)

    colour_check = image[sr][sc]
    cell_check(image, color, colour_check, sr, sc)

    return image

# =========== Solution 2 ========== #
# A more shorthand form of the solution above
def floodFill(image, sr, sc, color):
    
    r, c = len(image), len(image[0])
    new_colour = color
    colour = image[sr][sc]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c:
            return
        if image[i][j] == new_colour or image[i][j] != colour:
            return

        image[i][j] = new_colour

        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i,j+1)
        dfs(i, j-1)

    dfs(sr, sc)
    return image