class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hmap = new Map();

        for ( let i = 0; i < nums.length; i++ ) {

            if (hmap.has(nums[i])) {

                return true;
            }

            hmap.set(nums[i], i);
        }

        return false;
    }
}
