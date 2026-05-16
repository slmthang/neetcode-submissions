class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        total = 0

        i = 1
        
        while(i < len(height)):

            maxL = -1
            maxR = -1

            for j in range(0, i):
                
                if (height[j] > maxL):
                    maxL = height[j]
            
            for k in range(i + 1, len(height)):

                if (height[k] > maxR):
                    maxR = height[k] 

            value = min(maxL, maxR) - height[i]

            if (value > 0):
                total += value

            i += 1
        

        return total



