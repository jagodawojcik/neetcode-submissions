class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # 1. Scan through the arr to find closest element to x
        index_x = 0
        for i in range(len(arr)):
            if abs(arr[i] - x) < abs(arr[index_x] - x):
                index_x = i
        
        res = [arr[index_x]]
        # 2. Scan, left and right of index_x to find closes k nums
        l, r = index_x - 1, index_x + 1

        while len(res) < k:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        return sorted(res)

