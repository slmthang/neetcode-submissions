class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = left + ((right - left)//2)
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)

            if total <= h :
                if res > mid:
                    res = mid
                right = mid - 1
            else:
                left = mid + 1
        
            
            
        
        return res


        # 1 - len(piles) = min time
        # h = max time 


        
        
        # speed = 1

        # while True:
        #     total = 0

        #     for pile in piles:
        #         total += math.ceil(pile/speed)

        #     if total <= h:
        #         return speed

        #     speed += 1
        
        # return speed