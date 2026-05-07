from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        mini_grid = defaultdict(set) # a set where the keys =  (row/3, col/3)

        # traverse our 2d array/matrix
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
        # then check to see if the current number in the board is in the same row, or in the same col, or in the same smaller grid that we're in 
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or
                    board[row][col] in mini_grid[(row // 3, col // 3)]):    
                    return False
                # else we add our current number to our hashset for row, col, and the mini grid which is a pair of values
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                mini_grid[(row // 3, col // 3)].add(board[row][col])
        return True # finally return true since we've never found any dups