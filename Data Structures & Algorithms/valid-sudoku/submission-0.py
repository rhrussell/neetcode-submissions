class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)

        start_points = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for point in start_points:
            row_start = point[0]
            col_start = point[1]
            square_set = set()

            for i in range(row_start, row_start + 3, 1):
                for j in range(col_start, col_start + 3, 1):
                    if board[i][j] != ".":
                        # print("Row: " + str(i) + " Col: " + str(j) + " Element: " + str(board[i][j]))
                        if board[i][j] in square_set or board[i][j] in row_dict[i] or board[i][j] in col_dict[j]:
                            return False
                        else:
                            square_set.add(board[i][j])
                            row_dict[i].add(board[i][j])
                            col_dict[j].add(board[i][j])
            
        return True      