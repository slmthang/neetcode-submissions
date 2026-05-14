class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        if (s.length != t.length) {
            return false;
        }

        let smap = new Map();
        let tmap = new Map();

        for ( let i = 0; i < s.length; i++ ) {

            if (smap.has(s[i])) {

                smap.set(s[i], smap.get(s[i]) + 1);
            } else {
                smap.set(s[i], 1);
            }

            if (tmap.has(t[i])) {

                tmap.set(t[i], tmap.get(t[i]) + 1);
            } else {
                tmap.set(t[i], 1);
            }
        }

        for (const [key, value] of smap.entries()) {


            if (!(tmap.get(key) === value)) {
                return false
            }
        }


        return true;
    }
}
