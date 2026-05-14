class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        const arr = [];

    const obj = {};

    for ( let i = 0; i < strs.length; i++) {

        // split and join str
        let sortedStr = strs[i].split('').sort().join('');

        if (sortedStr in obj) {

            obj[sortedStr].push(strs[i]);
        } else {

            obj[sortedStr] = [strs[i]];
        }
    }

    for (let value of Object.values(obj)) {
        console.log(value)
        arr.push(value);
    }

    

    return arr;
    }
}
