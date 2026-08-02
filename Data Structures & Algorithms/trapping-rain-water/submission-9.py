class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0 
        max_left = height[0]
        max_right = height[-1]

        l, r = 0, len(height) - 1

        while l < r: 
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max(max_left - height[l], 0)
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max(max_right - height[r], 0)

        return res

        