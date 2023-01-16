var reorderList = function (head) {
    // fast-slow pointer determine the mid point
    let slow = head, fast = head
    while (fast !== null && fast.next !== null) {
        slow = slow.next
        fast = fast.next.next
    }

    // reverse the second half the linked list
    let prev = null, curr = slow
    while (curr !== null) {
        let temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    }

    // connect the nodes accordingly
    let end = prev, start = head
    while (end.next !== null) {
        let stemp = start.next
        let etemp = end.next
        start.next = end
        end.next = stemp
        start = stemp
        end = etemp
    }
    return head
};
