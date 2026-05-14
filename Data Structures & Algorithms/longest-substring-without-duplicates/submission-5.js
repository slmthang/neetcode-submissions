class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {

        if (s.length === 1) {
            return 1
        }

        if (s.length === 0) {
            return 0;
        }

        
        let max = 1;

        for (let i = 0; i < s.length - 1; i++) {

            let letters = [s[i]];
            let count = 1;

            for (let j = i + 1; j < s.length; j++) {

                if (letters.includes(s[j])) {
                    break;
                } else {
                    letters.push(s[j]);
                    count++;
                }
            }

            if (count > max) {
                max = count;
            }
        }

        return max
    }
}
