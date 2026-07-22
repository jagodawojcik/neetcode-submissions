class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top_row = 0
        bot_row = len(matrix) - 1

        while top_row <= bot_row:
            mid_row = top_row + (bot_row - top_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else: 
                break


        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[mid_row][m] == target:
                return True
            elif matrix[mid_row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
                
