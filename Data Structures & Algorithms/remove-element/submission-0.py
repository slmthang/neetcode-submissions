class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # In-Place Compaction ( Overwrite and Skip )
        # k = 0

        # for num in nums:

        #     if (num != val):
        #         nums[k] = num
        #         k += 1
        
        # return k

        # left = 0
        # right = len(nums) - 1

        # while (left <= right):

        #     if nums[left] == val:

        #         nums[left] = nums[right]
        #         nums[right] = nums[left]
        #         right -= 1
        #     else:
            
        #         left += 1
        
        # return left


        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return left