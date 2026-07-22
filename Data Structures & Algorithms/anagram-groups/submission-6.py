class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_hash = {}
        for s in strs:
            print(s)
            sorted_string = ''.join(sorted(s))
            print(type(sorted_string))
            if sorted_string in sorted_hash:
                sorted_hash[sorted_string].append(s)
            else:
                sorted_hash[sorted_string] = [s]

        
        return list(sorted_hash.values())






            
