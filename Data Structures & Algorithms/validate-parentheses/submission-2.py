class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for i in range(len(s)):

            if (s[i] not in hmap):
                stack.append(s[i])
            else:
                if len(stack) >= 1:
                    x = stack.pop()
                else:
                    return False

                if x != hmap[s[i]]:
                    return False

        
        return True if len(stack) == 0 else False