class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
        
    #     if (len(s) != len(t)):
    #         return False

    #     hashmap = {}

    #     for i in range(len(s)):
            
    #         if (s[i] in hashmap):
    #             hashmap[s[i]] += 1
    #         else:
    #             hashmap[s[i]] = 1
        
    #     for j in range(len(t)):
            
    #         if (t[j] in hashmap and hashmap[t[j]] >= 1):
    #             hashmap[t[j]] -= 1
    #         else:
    #             return False
        
    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0:
                return False

        return True
        
        