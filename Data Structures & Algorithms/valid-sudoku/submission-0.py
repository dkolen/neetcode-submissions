class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for i in range(len(board))]
        cols = [[0] * 9 for i in range(len(board))]
        boxes = [[0] * 9 for i in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    box = (row // 3) * 3 + (col // 3)
                    if rows[row][num - 1] or cols[col][num - 1] or boxes[box][num - 1]:
                        return False
                    rows[row][num - 1] = 1
                    cols[col][num - 1] = 1
                    boxes[box][num - 1] = 1
        return True

