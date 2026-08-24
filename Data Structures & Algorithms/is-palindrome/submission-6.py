class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     i = 0
    #     j = len(s) - 1

    #     while (i < j):

    #         while(i < j and not s[i].isalnum()):
    #             i += 1
            
    #         while(i < j and not s[j].isalnum()):
    #             j -= 1

    #         if (i < j and s[i].lower() != s[j].lower()):
    #             return False

    #         i += 1
    #         j -= 1
        
    #     return True

    # custom alp()
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while (i < j):

            while(i < j and not self.alp(s[i])):
                i += 1
            
            while(i < j and not self.alp(s[j])):
                j -= 1

            if (s[i].lower() != s[j].lower()):
                return False

            i += 1
            j -= 1
        
        return True

    def alp(self, c) -> bool:
        return (
            (ord(c) >= ord('a') and ord(c) <= ord('z')) or
            (ord(c) >= ord('A') and ord(c) <= ord('Z')) or
            (ord(c) >= ord('0') and ord(c) <= ord('9'))
        )