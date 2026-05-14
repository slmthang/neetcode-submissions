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
     * @return {ListNode}
     */
    reverseList(head) {

        if (!head) {
            return head;
        }

        let curNode = head;
        let prevNode = null;
        let isHead = true;

        while(curNode) {

            let nextNode = curNode.next;

            if (isHead) {
                curNode.next = null;
                prevNode = curNode;
                isHead = false;
            } else {

                curNode.next = prevNode;
                prevNode = curNode;
            }
            
            curNode = nextNode;
            

        }

        return prevNode;
    }
}
