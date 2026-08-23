class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for s in strs:
            seperator = str(len(s)) + "#" 
            encoded_str += seperator + s
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        numbers = "0123456789"
        while(i < len(s)):
            l = ""
            temp = ""
            while(s[i] in numbers):
                l += s[i]
                i += 1
            
            i += 1

            for j in range(int(l)):

                temp += s[i + j] 
            
            res.append(temp)
            i += int(l)
        
        return res
