class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;
        
        for (let i = 0; i < heights.length; i++) {
            let count = 0;

            for (let j = i + 1; j < heights.length; j++) {

                let minH;
                let dist = j - i;

                if (heights[i] > heights[j]) {
                    minH = heights[j];
                } else {
                    minH = heights[i];
                }

                count = minH * dist;

                if (count > max) {
                    max = count;
                }
            }
        }

        return max
    }
}
