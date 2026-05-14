class Node {
  constructor(key, value) {
    this.value = value
    this.key = key
    this.next = null
    this.prev = null
  }
}

class LRUCache {
  constructor(capacity) {
    this.capacity = capacity
    this.size = 0
    this.head = null
    this.tail = null
    this.map = new Map()
  }

  get(key) {
    if (this.map.has(key)) {
      let node = this.map.get(key)

      if (node === this.head && node !== this.tail) {
        this.head = this.head.next

        this.tail.next = node
        node.prev = this.tail
        node.next = null
        this.tail = node
      } else if (node !== this.head && node !== this.tail) {
        let prev = node.prev
        let next = node.next

        prev.next = next
        next.prev = prev

        this.tail.next = node
        node.prev = this.tail
        node.next = null
        this.tail = node
      }

      return node.value
    }

    return -1
  }

  put(key, value) {
    if (this.map.has(key)) {
      let node = this.map.get(key)

      node.value = value

      if (node === this.head && node !== this.tail) {
        this.head = this.head.next

        this.tail.next = node
        node.prev = this.tail
        node.next = null
        this.tail = node
      } else if (node !== this.head && node !== this.tail) {
        let prev = node.prev
        let next = node.next

        prev.next = next
        next.prev = prev

        this.tail.next = node
        node.prev = this.tail
        node.next = null
        this.tail = node
      }
    } else {
      let node = new Node(key, value)

      if (this.size === this.capacity) {
        let removedNode = this.head

        this.map.delete(removedNode.key)

        if (this.head === removedNode && this.tail === removedNode) {
          this.head = node
          this.tail = node
        } else {
          this.head = this.head.next
          this.head.prev = null

          this.tail.next = node
          node.prev = this.tail
          this.tail = node
        }

        this.size--
      } else {
        if (this.size === 0) {
          this.head = node
          this.tail = node
        } else {
          this.tail.next = node
          node.prev = this.tail
          this.tail = node
        }
      }
      this.map.set(key, node)

      this.size++
    }
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
