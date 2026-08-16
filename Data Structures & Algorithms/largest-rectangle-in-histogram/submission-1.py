class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # height, index, monotonic increasing
        max_area = 0

        for i, h in enumerate(heights):
            
            new_inx = i
            while stack and stack[-1][0] > h:
                max_area = max(max_area, (i - stack[-1][1]) * stack[-1][0])
                new_inx = stack[-1][1]
                stack.pop()

            stack.append((h, new_inx))

        while stack:
            max_area = max(max_area, (len(heights) - stack[-1][1]) * stack[-1][0])
            stack.pop()


        return max_area