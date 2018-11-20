getLastIndex() {
    let counter = 1;
    let current = this.head
    while(current.next) {
        current = current.next
        counter++;
    }

    return counter;
}

// pop an element off of the end of the linked list
pop() {
    if(!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        while(current.next){
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if(this.length === 0){
            this.head = null;
            this.tail = null;
        }
        return current;
}

// remove a node from the beginning of the linked list
shift() {
    if(!this.head) return undefined;
        let currentHead = this.head;
        this.head = currentHead.next;
        this.length--;
        if(this.length === 0){
            this.tail = null;
        }
        return currentHead;
}

// add a node to the beginning of the linked list
unshift(subject, amount) {
    let newNode = new Node(subject, amount);
        if(!this.head) {
            this.head = newNode;
            this.tail = this.head;
        }
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this;
}

// get values from an element at designated index
get(index) {
    if(index < 0 || index >= this.length) return null;
    let counter = 0;
    let current = this.head;

    while(counter !== index){
        current = current.next;
        counter++;
    }

    return current;
}

// set values for an element at designated index
set(index, subject, amount) {
    let foundNode = this.get(index);
        if(foundNode){
            foundNode.subject = subject;
            foundNode.amount = amount;
            return true;
        }
        return false;
}

// insert element at specific index
insert(index, subject, amount) {
    if(index < 0 || index > this.length) return false;
    if(index === this.length) return !!this.push(subject, amount)
    if(index === 0) return !!this.unshift(subject, amount)
    console.log("this is the length before insert" + this.length)
    let newNode = new Node(subject, amount)
    let prev = this.get(index - 1)
    let temp = prev.next

    prev.next = newNode
    newNode.next = temp;
    this.length++;

    return true;
}

// delete a node at a given index
delete(index) {
    if(index < 0 || index >= this.length) return undefined;
    if(index === 0) return this.shift();
    if(index === this.length - 1) return this.pop();

    let previousNode = this.get(index - 1);
    let removed = previousNode.next;

    previousNode.next = removed.next;
    this.length--;

    return removed;
}
