class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {

        let map = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }


        let stack = [];

        for (let i = 0; i < s.length; i++) {

            if (s[i] in map) {
                stack.push(s[i])
            } else if (map[stack.pop()] !== s[i]) {
                return false;
            }
        }

        return stack.length == 0;
    }
}
