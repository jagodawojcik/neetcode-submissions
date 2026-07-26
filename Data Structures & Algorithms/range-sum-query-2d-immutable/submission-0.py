class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sumMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                self.sumMatrix[r + 1][c + 1] = prefix + self.sumMatrix[r][c+1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1 - 1] - self.sumMatrix[row1 - 1][col2] + self.sumMatrix[row1 - 1][col1 - 1]
