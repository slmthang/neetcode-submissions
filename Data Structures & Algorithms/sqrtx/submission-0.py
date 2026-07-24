class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x

        while (left <= right):

            mid = left + ((right-left)//2)

            square = mid * mid

            if (square ==x):
                return mid

            elif (square > x):
                right = mid - 1
            
            elif (square < x):
                left = left + 1
            
        
        return right