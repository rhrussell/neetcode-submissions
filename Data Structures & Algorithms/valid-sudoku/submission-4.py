class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    # print("Row: " + str(i) + " Col: " + str(j) + " Element: " + str(board[i][j]))
                if board[r][c] in squares[(r // 3, c // 3)] or board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                else:
                    squares[(r // 3, c // 3)].add(board[r][c])
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
            
        return True      