class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        i = 1

        while (i < len(nums)):

            res[i] = res[i-1] * nums[i-1]
            i += 1
        
        j = len(nums) - 1
        suffix = 1
        while (j >= 0):

            res[j] *= suffix
            suffix *= nums[j]
            j -= 1
        
        return res