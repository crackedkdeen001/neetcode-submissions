class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_empty(digit):
            return digit == "."

        valid = False

        # for the row
        for row in board:
            dupli = set()
            for digit in row:
                if is_empty(digit):
                    continue
                if digit in dupli:
                    return valid
                dupli.add(digit)

        # for the column
        for i in range(len(board)):
            dupli = set()
            for row in board:
                digit = row[i]
                if is_empty(digit):
                    continue

                if digit in dupli:
                    return valid
                dupli.add(digit)

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):

                dupli = set()
                # to get the index of the values within each box
                # since each box is 3 x 3, we only loop 3 times
                for box_i in range(0, 3): # to get the row index within the box
                    for box_j in range(0, 3): # to get the column value within the box
                        digit = board[i + box_i][j + box_j]
                        if is_empty(digit):
                            continue
                        if digit in dupli:
                            return valid
                        dupli.add(digit)

        valid = True
        return valid