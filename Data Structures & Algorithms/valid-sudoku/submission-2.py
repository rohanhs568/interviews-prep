class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first solution attempt: check rules in order

        # rule 1 each row must conatin the digits 1-9 without duplicates

        for i in range(9):
            row_removed_dots = [x for x in board[i] if x != "."]
            if len(row_removed_dots) != len(set(row_removed_dots)):
                return False

        # Each column must contain the digits 1-9 without duplicates.

        for i in range(9):
            column_removed_dots = [board[j][i] for j in range(9) if board[j][i] != "."]

            if len(column_removed_dots) != len(set(column_removed_dots)):
                return False

        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

        for i in [0,3,6]:
            for j in [0,3,6]:
                square = [board[i+k][j+l] for k in range(3) for l in range(3) if board[i+k][j+l] != "."]

                if len(square) != len(set(square)):
                    return False

        return True

        
        