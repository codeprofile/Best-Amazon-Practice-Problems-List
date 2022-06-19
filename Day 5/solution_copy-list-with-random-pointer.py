class listnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def copyRandomList(head):
    if head is None:
        return head

    # Insert a new node with the same value after each node in the original list.

    curr = head
    while curr != None:
        new = listnode(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next

    # Now place the randompointer with the newly created node.

    curr = head
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next

    # Now Let us separate the newly created list from the original list.

    curr = head
    temp = head.next
    while curr.next != None:
        dummyHead = curr.next
        curr.next = curr.next.next
        curr = dummyHead

    return temp


def printList(head):
    curr = head
    while curr != None:
        print(curr.data, " ", curr.random.data)
        curr = curr.next


if __name__ == "__main__":
    head = listnode(1)
    head.next = listnode(2)
    head.next.next = listnode(3)
    head.next.next.next = listnode(4)
    head.next.next.next.next = listnode(5)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next

    head.next.next.next.random = head.next.next.next.next
    head.next.next.next.next.random = head.next
    print("Original list:\n")
    printList(head)

    copiedList = copyRandomList(head)

    print("\n Deep Copy of the List:")
    printList(copiedList)
