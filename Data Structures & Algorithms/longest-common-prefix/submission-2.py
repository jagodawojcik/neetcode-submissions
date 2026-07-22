class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        first_str = strs[0]
        common_prefix = ""
        for i in range(len(first_str)):
            common_prefix += first_str[i]
            for s in strs[1:]:
                if s[:i+1] != common_prefix:
                    return common_prefix[:i]

        return common_prefix