class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;
        
    let p1 = 0;
    let p2 = heights.length - 1;

    while (p1 < p2) {

        let size = 0;
        let min = 0;
        let dist = p2-p1;

        if (heights[p1] > heights[p2]) {
            min = heights[p2]
            p2--;
        } else {
            min = heights[p1]
            p1++;
        }

        size = dist * min

        if (size > max) {
            max = size
        }


    }


    return max
    }
}
