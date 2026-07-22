class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = defaultdict(list) # keys: freq list of characters, vals: list of strings

        for s in strs:
            freq_list = [0] * 26 # a ... z count
            for c in s:
                freq_list[ord(c) - ord('a')] += 1
            freq_map[tuple(freq_list)].append(s)

        return list(freq_map.values())
