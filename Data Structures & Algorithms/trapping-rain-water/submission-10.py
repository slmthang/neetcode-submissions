class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if not height:
        #     return 0

        # total = 0

        # i = 1
        
        # while(i < len(height)):

        #     maxL = -1
        #     maxR = -1

        #     for j in range(0, i):
                
        #         if (height[j] > maxL):
        #             maxL = height[j]
            
        #     for k in range(i + 1, len(height)):

        #         if (height[k] > maxR):
        #             maxR = height[k] 

        #     value = min(maxL, maxR) - height[i]

        #     if (value > 0):
        #         total += value

        #     i += 1
        

        # return total

        ### PreFix ###

        # left_max = [-1] * len(height)
        # right_max = [-1] * len(height)

        # largest = -1

        # for i in range(len(height)):
            
        #     if (height[i] > largest):
        #         largest = height[i]   
            
        #     left_max[i] = largest
        
        # largest = -1

        # for i in range(len(height)-1, -1, -1):
            
        #     if (height[i] > largest):
        #         largest = height[i]
            
        #     right_max[i] = largest
        
        # total = 0
        # for i in range(len(height)):

        #     total += min(left_max[i], right_max[i]) - height[i]
        
        # return total


        ### 2 Pointers ###

        l = 0
        r = len(height) - 1
        total = 0
        maxR = 0
        maxL = 0

        while (l < r):

            if (height[l] > height[r]):

                if (height[r] > maxR):
                    maxR = height[r]
                
                total += maxR - height[r]
                
                r -= 1
            else:

                if (height[l] > maxL):
                    maxL = height[l]
                
                total += maxL - height[l]
                
                l += 1
            
        return total
            






