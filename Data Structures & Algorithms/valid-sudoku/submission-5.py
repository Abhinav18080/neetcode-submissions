class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = (square//3)*3+i
        # cols = (square%3)*3+j

        # check rows
        for row in range(9):
            seen = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])

        # check cols
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])

        # check square
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    rows = (square//3)*3+i
                    cols = (square%3)*3+j
                    if board[rows][cols] == ".":
                        continue
                    if board[rows][cols] in seen:
                        return False
                    seen.add(board[rows][cols])
        return True