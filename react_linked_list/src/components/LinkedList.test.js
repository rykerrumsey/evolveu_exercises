import { LinkedList } from './LinkedList';

describe('test the functionality of the linked list', () => {
    let ll;

    beforeEach(() => {
        ll = new LinkedList("a", 1);
        ll.add("b", 2);
        ll.add("c", 3);
    })

    test('should init a node in linked list', () => {
        expect(ll.head.subject).toBe('a')
        expect(ll.head.amount).toBe(1)
        expect(ll.length).toBe(3)
    })

    test('should add one node to the end of the linked list', () => {
        ll.add('d', 4)
        expect(ll.tail.subject).toBe('d')
        expect(ll.tail.amount).toBe(4)
        expect(ll.length).toBe(4)
    })

    test('should insert a node after current node', () => {
        let currentNode = ll.head
        let success = ll.insert(currentNode, "inserted", 2)
        expect(success).toBeTruthy()
        expect(currentNode.next.subject).toBe('inserted')
        expect(currentNode.next.amount).toBe(2)
    })

    test('should delete current node from linked list', () => {
        let currentNode = ll.head
        let nextNode = currentNode.next
        ll.delete(nextNode)
        expect(ll.length).toBe(2)
        expect(currentNode.next.subject).toBe('c')
        expect(currentNode.next.amount).toBe(3)
    })

    test('should return the first element in the linked list', () => {
        let first = ll.first()
        expect(first.subject).toBe('a')
        expect(first.amount).toBe(1)
    })

    test('should return the last element in the linked list', () => {
        let last = ll.last()
        expect(last.subject).toBe('c')
        expect(last.amount).toBe(3)
    })

    test('should return the next element in the linked list', () => {
        let currentNode = ll.head
        currentNode = ll.next(currentNode)
        expect(currentNode.subject).toBe('b')
        expect(currentNode.amount).toBe(2)
        currentNode = ll.next(currentNode)
        expect(currentNode.subject).toBe('c')
        expect(currentNode.amount).toBe(3)
        currentNode = ll.next(currentNode)
        expect(currentNode.subject).toBe('a')
        expect(currentNode.amount).toBe(1)
    })

    test('should return the previous element in the linked list', () => {
        let currentNode = ll.head
        expect(ll.prev(currentNode).subject).toBe('c')
        expect(ll.prev(currentNode).amount).toBe(3)
        let nextNode = currentNode.next
        let prevNode = ll.prev(nextNode)
        expect(prevNode.subject).toBe('a')
        expect(prevNode.amount).toBe(1)
    })
})


