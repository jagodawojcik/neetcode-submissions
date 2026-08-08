class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # Start at window size of len(arr), shrink either form left or right depeding on
        # whether arr[l] or arr[r] is further away from x

        l, r = 0, len(arr) - 1

        while (r - l + 1) > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1

        
        return arr[l:r+1]


