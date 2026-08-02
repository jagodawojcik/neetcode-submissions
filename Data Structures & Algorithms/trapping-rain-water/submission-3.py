class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0 
        # height=[0,2,0,3,1,0,1,3,2,1]
        max_left = [0] #0,0,2,2,3,3,3,3,..
        max_right = [0] #0,1,2,3,3,3,3,..

        for h in height:
            max_left.append(max(max_left[-1], h))
        for h in height[::-1]:
            max_right.append(max(max_right[-1], h))
            
        for i, h in enumerate(height):
            res += max(min(max_left[i], max_right[-i-1]) - h, 0)

        return res

        