class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class Deque {
    constructor() {
        this.head = new Node(-1);
        this.tail = new Node(-1);

        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        if (this.head.next === this.tail) {
            return true;
        } 

        return false;
    }

    /**
     * @param {number} value
     */
    append(value) {

        let newNode = new Node(value);

        // prev
        let prevTail = this.tail.prev;
        newNode.prev = prevTail;
        newNode.next = this.tail;
        prevTail.next = newNode;
        this.tail.prev = newNode;
        
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {

        let newNode = new Node(value);

        // prev
        let prevHead = this.head.next;
        newNode.next = prevHead;
        newNode.prev = this.head;
        prevHead.prev = newNode;
        this.head.next = newNode;
    }

    /**
     * @return {void}
     */
    pop() {

        if (this.isEmpty()) {
            return -1;
        }

        let popped = this.tail.prev;

        // new tail
        let newTail = popped.prev;
        this.tail.prev = newTail;
        newTail.next = this.tail;

        return popped.value;
    }

    /**
     * @return {number}
     */
    popleft() {

        if (this.isEmpty()) {
            return -1;
        }

        let popped = this.head.next;

        // new head
        let newHead = popped.next;
        this.head.next = newHead;
        newHead.prev = this.head;
        

        return popped.value;
    }
}
