class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # sort (n log n)
        # nums.sort()

        # mid = len(nums)//2

        # return nums[mid]

        # # Boyer–Moore Majority Vote ( Mine )
        # candidate = nums[0]
        # count = 1

        # for i in range(1, len(nums)):
            
        #     if count == 0:
        #         candidate = nums[i]

        #     if nums[i] == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        
        # return candidate

        # Boyer-Moore Majority
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate