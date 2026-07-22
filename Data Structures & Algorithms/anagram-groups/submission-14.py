class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 26 alphabet letters a...z

        mapping = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord("a")] += 1
            
            mapping[tuple(count)].append(string)

        return list(mapping.values())






            
