class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {

        if (s1.length > s2.length) {
            return false
        }

        let p1 =0;
        let s1Arr = s1.split('').sort().join('');
        
        while (p1 + s1.length - 1 < s2.length) {
            // console.log(p1);

            let tempArr = '';

            for (let j = 0; j < s1.length; j++) {
                // console.log(s2[j], p1)
                tempArr += s2[p1+j];
                // console.log(s2[j]
            }
            // console.log(s1Arr + "|" + tempArr);
            tempArr = tempArr.split('').sort().join('');

            

            if (tempArr === s1Arr) {
                return true;
            }

            p1++;
        }

        return false;
    }
}
