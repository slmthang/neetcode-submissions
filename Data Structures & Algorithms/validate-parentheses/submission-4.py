class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hmap = {
            "]" :"[",
            ")" : "(",
            "}" : "{"
        }

        for i in range(len(s)):

            if (s[i] not in hmap):
                stack.append(s[i])
            else:

                if (not stack or stack.pop() != hmap[s[i]] ):
                    return False
            
        
        return True if not stack else False