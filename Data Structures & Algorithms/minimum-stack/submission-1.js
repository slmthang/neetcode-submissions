class MinStack {
    constructor() {
        this.stack = [];
        this.min = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);

        // update min if matches
        if (this.min.length === 0) {
            this.min.push(val);
        } else {
            if (this.min[this.min.length - 1] >= val) {
                
                this.min.push(val);
            }
        }
    }

    /**
     * @return {void}
     */
    pop() {
        let p = this.stack.pop();

        if (p === this.min[this.min.length -1] ) {
            this.min.pop();
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length-1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min[this.min.length - 1];
    }
}
