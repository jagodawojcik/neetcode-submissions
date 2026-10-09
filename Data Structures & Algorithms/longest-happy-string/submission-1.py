class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        freq_heap = []
        for count, char in [[-a, 'a'], [-b, 'b'], [-c, 'c']]:
            if count != 0:
                freq_heap.append([count, char])

        heapq.heapify(freq_heap)

        res = ""
        while freq_heap:
            count, char = heapq.heappop(freq_heap)
            
            if len(res) > 1 and char == res[-1] and char == res[-2]:
                if freq_heap:
                    count2, char2 = heapq.heappop(freq_heap)
                    res += char2
                    count2 += 1

                    if count2 != 0:
                        heapq.heappush(freq_heap, [count2, char2])
                else:
                    break
            
            else:
                res += char # cc
                count += 1
            
            if count != 0:
                heapq.heappush(freq_heap, [count, char])
        
        return res

    
