def setZeroes(matrix):
    
    # Variables to track if we need to zero out the row / col
    # That we are storing what rows / col we need to zero out
    zero_row = False
    zero_col = False
    
    num_rows = len(matrix)   # Define the number of rows based on hopw many lists
    num_cols = len(matrix[0]) # Define number of columns based on how many elements
    
    for row in range(num_rows):
        for col in range(num_cols):
            # Checks if its first row / col for later to change to zeroes if needed
            if matrix[row][col] == 0:
                if row == 0:
                    zero_row = True
                if col == 0:
                    zero_col = True
    
                # Set the zeroth column / row to hold zeroes of which ones to zero out
                matrix[row][0] = 0
                matrix[0][col] = 0

    # iterate through matrix to update the cell to be zero if its row / col has been marked
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0
    
    #  Zero out the first row / column if they had a zero there originally
    if zero_row:
        for col in range(num_cols):
            matrix[0][col] = 0
    
    if zero_col:
        for row in range(num_rows):
            matrix[row][0] = 0
       
    return matrix

        
if __name__ == "__main__":
    print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))