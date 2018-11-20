export class Node {
    constructor(subject, amount) {
        this.subject = subject;
        this.amount = amount;
        this.next = null;
        this.prev = null;
    }
}

export class LinkedList {
    constructor(subject, amount) {
        this.head = new Node(subject, amount)
        this.length = 1;
        this.tail = this.head;
    }

    // add an element to the end of the linked list
    add(subject, amount) {
        const node = new Node(subject, amount);

        if (!this.head) {
          this.head = node;
          this.tail = this.head;
        } else {
            this.tail.next = node;
            node.prev = this.tail
            this.tail = node;
        }
        this.length += 1;

        return node
    }

    delete(node) {
       if(node === null) return false
       let previousNode = node.prev
       let nextNode = node.next

       previousNode.next = nextNode
       nextNode.prev = previousNode
       this.length--

       return true
    }

    insert(node, subject, amount) {
        if(node.next === null) return false

        const insertedNode = new Node(subject, amount)
        const tail = node.next

        tail.prev = insertedNode
        insertedNode.next = tail
        insertedNode.prev = node
        node.next = insertedNode
        this.length++;

        return true
    }

    last() {
        return this.tail
    }

    first() {
        return this.head
    }

    next(node) {
        if(node.next === null) return this.head
        return node.next 
    }

    prev(node) {
        if(node.prev === null) return this.tail
        return node.prev
    }
}
