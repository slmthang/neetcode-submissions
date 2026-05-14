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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        
        let head;
        let prevNode;
        let isHead = true;

        if (list1 && list2) {
            
            while (list1 && list2) {
                if (list1.val <= list2.val) {
                    if (isHead) {
                        head = list1;
                        isHead = false;
                        prevNode = head;
                    } else {
                        prevNode.next = list1;
                        prevNode = list1;
                    }
                    list1 = list1.next;
                } else {

                    if (isHead) {
                        head = list2;
                        isHead = false;
                        prevNode = head;
                    } else {
                        prevNode.next = list2;
                        prevNode = list2;
                    }

                    list2 = list2.next;
                }
            }

            if (list1) {
                prevNode.next = list1;
            } else if (list2) {
                prevNode.next = list2;
            }

        } else if (list1 && !list2) {
            return list1;
        } else if (!list1 && list2) {
            return list2;
        } else {
            return null;
        }

        return head;
    }
}
