class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t : t[1])
        
        cur_psg = 0
        min_heap = []
        for t in trips:
            num_psg, from_pos, to_pos = t

            while min_heap and min_heap[0][0] <= from_pos:
                cur_psg -= heapq.heappop(min_heap)[1]


            heapq.heappush(min_heap, [to_pos, num_psg])
            cur_psg += num_psg
            if cur_psg > capacity:
                return False

        return True