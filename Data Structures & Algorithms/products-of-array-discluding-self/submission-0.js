class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let res = [];

        for (let i = 0; i < nums.length; i++) {

            let total = 1;
            for (let j = 0; j < nums.length; j++) {

                if (j !== i) {
                    total *=  nums[j];
                }
            }

            res.push(total)
        }

        return res
    }
}
