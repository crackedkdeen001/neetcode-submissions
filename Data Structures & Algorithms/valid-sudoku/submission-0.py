class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_empty(sqaure):
            if square == ".":
                return True
            return False

        valid = False
        for row in board:
            seen = set()
            for square in row:
                if is_empty(square):
                    continue

                if square in seen:
                    return valid
                seen.add(square)
        
        n = len(board)
        for i in range(n):
            seen = set()
            for row in board:
                square = row[i]
                if is_empty(square):
                    continue

                if square in seen:
                    return valid
                seen.add(square)

        box_size = 3
        for row in range(0, n, box_size):
            for column in range(0, n, box_size):
                seen = set()
                for box_row_idx in range(box_size):
                    for box_column_idx in range(box_size):
                        square = board[row + box_row_idx][column + box_column_idx]

                        if is_empty(square):
                            continue

                        if square in seen:
                            return valid
                        seen.add(square)

        valid = True
        return valid



    
                    