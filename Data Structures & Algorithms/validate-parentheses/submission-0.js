class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
    
        let obj = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for (let i = 0; i < s.length; i++ ) {

            // if opening bracket
            if ( Object.keys(obj).includes(s[i]) ) {

                // push to the stack
                stack.push(s[i]);
            } else {  // if closing bracket

                if ( obj[stack.pop()] !== s[i]) {
                    return false;
                }
            }
        }

        return stack.length == 0;
    }

    // var isValid = function(s) {   
    //     const stack = [];
        
    //     for (let i = 0 ; i < s.length ; i++) {
    //         let c = s.charAt(i);
    //         switch(c) {
    //             case '(': stack.push(')');
    //                 break;
    //             case '[': stack.push(']');
    //                 break;
    //             case '{': stack.push('}');
    //                 break;
    //             default:
    //                 if (c !== stack.pop()) {
    //                     return false;
    //                 }
    //         }
    //     }
        
    //     return stack.length === 0;
    // };
}





