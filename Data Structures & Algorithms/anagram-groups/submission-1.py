class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        res = []

        for s in strs:

            ss = "".join(sorted(s))

            if (ss in groups):
                groups[ss].append(s)
            else:
                groups[ss] = [s]
        
        for v in groups.values():

            res.append(v)
        
        return res

