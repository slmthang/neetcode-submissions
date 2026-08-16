from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sorted approach
        # groups = {}
        # res = []

        # for s in strs:

        #     ss = "".join(sorted(s))

        #     if (ss in groups):
        #         groups[ss].append(s)
        #     else:
        #         groups[ss] = [s]
        
        # for v in groups.values():

        #     res.append(v)
        
        # return res

        ### ch freq approach
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch)-ord('a')] += 1
            groups[tuple(freq)].append(s)
        
        return list(groups.values())