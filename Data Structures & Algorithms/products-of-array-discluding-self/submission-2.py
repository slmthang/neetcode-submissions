class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = [1] * len(nums)

        prefix[0] = nums[0]

        for i in range(1, len(nums)):

            prefix[i] = prefix[i-1] * nums[i]
        
        suffix = [1] * len(nums)

        suffix[len(nums)-1] = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):

            suffix[i] = suffix[i+1] * nums[i]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < len(nums) - 1 else 1

            res[i] = left * right

        return res 

        