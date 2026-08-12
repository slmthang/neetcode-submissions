class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()

        for i in range(len(nums)):

            if nums[i] in found:
                return True
            else:
                found.add(nums[i])

        return False