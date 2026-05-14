class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let map = {};

        for (let i = 0; i < 9; i++) {

            for (let j = 0; j < 9; j++) {

                let x = Math.floor(j/3) + '' + Math.floor(i/3) ;

                if (x in map) {
                    
                    if (map[x].includes(board[i][j]) && board[i][j] !== '.') {
                        return false;
                    }

                    
                } else {
                    map[x] = [];
                }

                if (i + 'i' in map) {
                    
                    if (map[i + 'i'].includes(board[i][j]) && board[i][j] !== '.') {
                        return false;
                    }

                    
                } else {
                    map[i + 'i'] = [];
                }


                if (j + 'j' in map) {
                    
                    if (map[j + 'j'].includes(board[i][j]) && board[i][j] !== '.') {
                        return false;
                    }

                    
                } else {
                    map[j + 'j'] = [];
                }

                map[x].push(board[i][j])
                map[i + 'i'].push(board[i][j])
                map[j + 'j'].push(board[i][j])
            }
        }
        
        return true
    }
}
