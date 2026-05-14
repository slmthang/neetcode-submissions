/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {

        if (!head) {
            return null;
        }

        let map = {};
        let index = 0;

        while (head) {

            if (head.val in map) {
                return true;
            }

            map[head.val] = index;
            index++;
            head = head.next;
        }

        return false;
    }
}
