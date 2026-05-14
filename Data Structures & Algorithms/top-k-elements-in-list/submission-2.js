class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = {};

    for (let i = 0; i < nums.length; i++) {

        if (!(nums[i] in map)) {

            map[nums[i]] = 1;
        } else {
            map[nums[i]] += 1;
        }

    }

    // map -> list
    let entries = Object.entries(map);

    // sort : large to small
    entries.sort((a,b) => b[1] - a[1]);

    // list to output
    let x = [];

    // only output k outputs
    for (let i = 0; i < k; i++) {
        x.push(entries[i][0]);
    }

    return x;
    }
}
