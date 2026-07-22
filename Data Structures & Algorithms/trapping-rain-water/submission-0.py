class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [0]
        right_max = [0]

        for i in range(len(height)):
            left_max.append(max(height[i], left_max[-1]))
            right_max.append(max(height[len(height) - 1 - i], right_max[-1]))
        
        trapped_water = 0
        for i in range(len(height)):
            water = min(left_max[i], right_max[len(height) - 1 - i]) - height[i]
            if water > 0:
                trapped_water += water
            
        return trapped_water
        
            