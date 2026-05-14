class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.arr = [];
        this.length = 0;
        this.capacity = capacity;
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        if ( i >= 0 && i < this.length && i < this.capacity) {
            return this.arr[i];
        }
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.arr[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {

        if (this.length + 1 <= this.capacity) {
            this.arr[this.length] = n;
            this.length++;  
        } else {
            this.resize();
            this.arr[this.length] = n;
            this.length++;
        }
        
    }

    /**
     * @returns {number}
     */
    popback() {
        let n = this.arr[this.length-1];
        this.arr[this.length-1] = null;
        this.length--;
        return n;
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity = 2 * this.capacity;
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.length;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity;
    }
}
