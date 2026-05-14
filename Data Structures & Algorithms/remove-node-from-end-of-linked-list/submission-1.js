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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {

        let cur = head;
        let cur1 = head;
        let len = 0;

        while (cur1) {

            len++;
            cur1 = cur1.next;
        }

        const r = len - n;

        if (r===0) {
            return head.next;
        }


            for (let i = 0; i < r; i++) {

                if (i + 1 === r) {
                    cur.next = cur.next.next;
                    break;
                }

                cur = cur.next;
            }

        return head;
    }
}
