class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = [0, 0, 0]

        for e in nums:
            counts[e] += 1

        k = 0

        for i in range(3):

            for j in range(counts[i]):

                nums[k] = i
                k += 1

        return nums
