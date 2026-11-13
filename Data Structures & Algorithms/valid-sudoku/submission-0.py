class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        check_row = all(len(rows := [x for x in row if x != "."]) == len(set(rows)) for row in board)

        if not check_row:
            return check_row

        check_col = all(len(cols := [x for x in col if x != "."]) == len(set(cols)) for col in zip(*board))

        if not check_col:
            return check_col

        r,c = 0,0

        check_sqr = all(
            len(
                nums := [
                    board[i][j]
                    for i in range(r,r+3)
                    for j in range(c, c+3)
                    if board[i][j] != "."
                ]
            )
            ==len(set(nums))
            for r in (0, 3, 6)
            for c in (0, 3, 6)
        )

        return check_sqr
        