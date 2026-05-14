class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let obj = {};

        const dfs = (i) => {
            let result = 0;
            if ( i <= 3 ) {
                result = i
            } else {
                result = dfs(i - 1) + dfs(i - 2)
            }

            obj[i] = result;

            return result;
        }

        return dfs(n)
    }
}
