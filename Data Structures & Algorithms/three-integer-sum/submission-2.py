class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        duplicates = []
        nums.sort()
        # starts with i

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while (l < r):

                if ((nums[l] + nums[r] + nums[i] == 0)):
                    if ([nums[l], nums[r], nums[i]] not in duplicates):
                        result.append([nums[l], nums[r], nums[i]])
                        duplicates.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif (nums[l] + nums[r] + nums[i] > 0):
                    r -= 1
                else:
                    l += 1
        return result


