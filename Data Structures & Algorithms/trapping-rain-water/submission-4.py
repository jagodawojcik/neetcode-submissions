class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0 
        max_left = [0]
        max_right = [0]

        for i in range(len(height)):
            max_left.append(max(max_left[-1], height[i]))
            max_right.append(max(max_right[-1], height[-i - 1]))

        for i, h in enumerate(height):
            res += max(min(max_left[i], max_right[-i-1]) - h, 0)

        return res

        