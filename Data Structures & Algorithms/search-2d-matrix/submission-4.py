class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        target_row = 0
        while l <= r:
            mid_row = (l + r) // 2
            if target > matrix[mid_row][-1]:
                l = mid_row + 1
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                target_row = mid_row
                break

        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if target == matrix[target_row][m]:
                return True
            elif target > matrix[target_row][m]:
                l = m + 1
            else:
                r = m - 1

        return False



