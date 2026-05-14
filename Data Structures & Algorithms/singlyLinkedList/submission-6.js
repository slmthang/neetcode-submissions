
class ListNode {

    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}


class LinkedList {

    constructor() {
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {

        let i = 0;
        let cur = this.head.next;

        while (cur) {

            if (index == i) {
                return cur.val;
            }

            cur = cur.next;
            i++;
        }

        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {

        let newNode = new ListNode(val);
        let prevHead = this.head.next;

        if (prevHead) {

            this.head.next = newNode;
            newNode.next = prevHead;
        } else {
            
            this.head.next = newNode;
            this.tail = newNode;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {

        let newNode = new ListNode(val);

        this.tail.next = newNode;
        this.tail = newNode;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let prev = this.head;
        let cur = this.head.next;

        while (cur) {

            if (index == i) {

                if (cur === this.tail ) {

                    prev.next = null;
                    this.tail = prev;
                } else {
                    // remove
                    prev.next = cur.next;
                }
                

                return true;
            }
            
            prev = cur;
            cur = cur.next;
            i++;
        }

        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {

        let arr = [];

        let cur = this.head.next;

        while (cur) {

            arr.push(cur.val);
            cur = cur.next;
        }

        return arr;
    }
}
