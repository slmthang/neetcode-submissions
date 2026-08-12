class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = n * 2
        ans = size * [None]

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans