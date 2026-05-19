class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        for i in range(len(s)):
            fs = {}
            maxf = 0

            for j in range(i, len(s)):
                
                if (s[j] in fs):
                    fs[s[j]] += 1
                else:
                    fs[s[j]] = 1

                if (fs[s[j]] > maxf):
                    maxf = fs[s[j]]
                
                winSize = j - i + 1

                if (winSize) - maxf <= k:
                    
                    if (winSize > res):
                        res = winSize
        
        return res
                    
                


        

            

                

            
            

                

            

            
         
