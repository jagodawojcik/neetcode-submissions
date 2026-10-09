class Solution:
    def reorganizeString(self, s: str) -> str:
        
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1

        freq_heap = [[-count, char] for char, count in char_freq.items()]
        heapq.heapify(freq_heap)
        
        prev = None
        res = ""
        while freq_heap or prev:
            if prev and not freq_heap:
                return ""

            count, char = heapq.heappop(freq_heap)
            res += char
            count += 1

            if prev:
                heapq.heappush(freq_heap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return res


            



