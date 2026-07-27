class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # key: col indx, val: seen sudoku entries
        squares = defaultdict(set) # key: (row, col) index // 3, val: seen entries

        for i, row in enumerate(board):
            rows_set = set()
            for j, col in enumerate(row):
                if col == ".":
                    continue
                    
                if col in rows_set:
                    return False
                rows_set.add(col)

                if col in cols[j]:
                    return False
                cols[j].add(col)

                if col in squares[(i//3, j//3)]:
                    return False
                squares[(i//3, j//3)].add(col)

        return True

