class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        trapped_water = 0

        while l < r:

            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                water = max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                water = max_right - height[r]

            trapped_water += water
        
        return trapped_water
        
            