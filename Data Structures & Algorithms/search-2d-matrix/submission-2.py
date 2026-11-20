class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # we searching rows using binary search and the 
        # first and last elements of each row as the boundaries
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                # we break if we've found our target ro
                break

        print(top, bottom)
        if top > bottom:
            return False


        # we now perform binary search on the supposed row
        # target belongs in
        l = 0
        r = COLS - 1
        target_row = matrix[row]
        while l <= r:
            mid = (l + r) // 2
            if target_row[mid] > target:
                r = mid - 1
            elif target_row[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
