class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ORIGINAL
        # if (len(strs) <= 1):
        #     return strs[0]

        # based_string = strs[0]
        # common = float('infinity')
        # for i in range(1, len(strs)):

        #     count = 0

        #     for j in range(min(len(based_string), len(strs[i]))):

        #         if (based_string[j] == strs[i][j]):
        #             count += 1
        #         else:
        #             break
            
        #     common = min(count, common)

        # return based_string[:common]

        # OPTIMIZED ( NOT MINE )
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            # shrink prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix