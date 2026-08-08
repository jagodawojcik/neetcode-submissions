class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        freq_map_s1 = defaultdict(int)
        freq_map_s2 = defaultdict(int)

        for i in range(len(s1)):
            freq_map_s1[s1[i]] += 1
            freq_map_s2[s2[i]] += 1

        if  freq_map_s1 == freq_map_s2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            freq_map_s2[s2[r]] += 1
            freq_map_s2[s2[l]] -= 1

            if freq_map_s2[s2[l]] == 0:
                del freq_map_s2[s2[l]]

            if freq_map_s1 == freq_map_s2:
                return True
            
            l += 1

#         s1="ab"
#         s2="lecabee"



        return False

        

