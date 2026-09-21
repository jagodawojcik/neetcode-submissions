class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        len_arr = mountainArr.length()
        # 1. Find mountain peak
        
        l, r = 0, len_arr - 1
        while l <= r:
            m = (l + r) // 2

            if m - 1 < 0 or m + 1 > len_arr - 1:
                break
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left <= mid >= right:
                break
            elif left >= mid >= right: # decreasing slope
                r = m - 1
            else:
                l = m + 1
        peak = m
        
        # 2. Search left range (increasing), [:m]
        l, r = 0, m

        while l <= r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid > target:
                r = m - 1
            else:
                l = m + 1

        # 3. Search right range (decreasing), [m:]
        l, r = m, len_arr - 1

        while l <= r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                r = m - 1
            else:
                l = m + 1

        return -1


