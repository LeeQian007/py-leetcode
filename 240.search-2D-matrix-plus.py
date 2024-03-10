class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        x, y = ROWS - 1, 0  # 18
        while x >= 0 and y < COLS:
            if target == matrix[x][y]:
                return True
            if target < matrix[x][y]:
                x -= 1
            else:
                y += 1
        return False
