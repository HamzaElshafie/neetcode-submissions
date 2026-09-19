class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs_1 = {}
        for c in s1:
            freqs_1[c] = 1 + freqs_1.get(c, 0)
        
        for i in range(len(s2)):
            freqs_2, count = {}, 0
            for j in range(i, len(s2)):
                freqs_2[s2[j]] = 1 + freqs_2.get(s2[j], 0)
                if freqs_1.get(s2[j], 0) < freqs_2.get(s2[j], 0):
                    break
                if freqs_1.get(s2[j], 0) == freqs_2.get(s2[j], 0):
                    count += 1
                
                if count == len(freqs_1):
                    return True

        return False
        
       

      