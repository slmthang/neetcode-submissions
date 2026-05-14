class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {

        if (nums.length === 1) {
            return 1;
        }

        nums.sort((a, b) => a - b)
        let res = 0;

        let cur = nums[0];
        let i = 0;
        let streak = 0;

        while (i < nums.length) {

            if (nums[i] !== cur) {
                cur = nums[i]
                streak = 0
            }

            while (i < nums.length && nums[i] === cur) {
                i++;
            }

            streak++;
            cur++;
            
            if (streak > res) {
                res = streak
            }
        }
        return res;

    }
}
