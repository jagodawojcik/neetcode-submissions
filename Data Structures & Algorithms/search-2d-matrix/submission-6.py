class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        mid_row = 0
        while l <= r:
            mid_row = (l + r) // 2
            if target < matrix[mid_row][0]:
                r = mid_row - 1
            elif target > matrix[mid_row][-1]:
                l = mid_row + 1
            else:
                break
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid_row][mid]:
                r = mid - 1
            elif target > matrix[mid_row][mid]:
                l = mid + 1
            else:
                return True

        return False

