class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Iterate through each row and column and use a set to keep track of seen values.
        For the 3x3 sub-grids:
            - Iterate through each of the 9 sub-grids.
            - Use integer division and modulus to determine the starting row and column of each sub-grid.
            - Loop through the 3x3 section and check for duplicate values.
        """
        # Checking each number in each row
        for row in range(9):
            seen = set()
            for i in range(9):  # Loop through columns (left to right)
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])  # else add num to the set 
        
        # Checking each number in each column
        for col in range(9):
            seen = set()
            for j in range(9):  # Loop through rows (top to bottom)
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        
        # Loop through each of the 9 mini-grids
        for mini_grid in range(9):
            seen = set()
            for i in range(3):  
                for j in range(3):
                    # Calculate the row index for the current mini-grid
                    row = (mini_grid // 3) * 3 + i  
                    # (mini_grid // 3) finds which row of sub-grids we are in.
                    # Multiply by 3 to get the actual starting row index for that sub-grid.
                    # + i moves within the sub-grid.

                    # Calculate the column index for the current mini-grid
                    col = (mini_grid % 3) * 3 + j  
                    # (mini_grid % 3) finds which column of sub-grids we are in.
                    # Multiply by 3 to get the actual starting column index for that sub-grid.
                    # + j moves within the sub-grid.

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True  # return True when no duplicates are found in rows, columns, or sub-grids.
