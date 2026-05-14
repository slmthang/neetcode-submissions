class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let alpha = 'abcdefghijklmnopqrstuvwxyz0123456789';

    let cleaned = '';

    for (let i = 0; i < s.length; i++) {
        if (alpha.includes(s[i].toLowerCase())) {
            cleaned += s[i].toLowerCase()
        }
    }

    let p1 = 0;
    let p2 = cleaned.length - 1;

    while (p1 <= p2) {

        if (!(cleaned[p1] == cleaned[p2])) {

            return false;
        }

        p1++;
        p2--;
    }

    return true;
    }
}
