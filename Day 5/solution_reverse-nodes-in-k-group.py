# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Helper function to print linked list starting from the current node
    def print(self):
        ptr = self
        while ptr:
            print(ptr.data, end=' —> ')
            ptr = ptr.next

        print('None')


# Function to reverse every group of `k` nodes in a given linked list
def reverseInGroups(head, k):
    """
    problem statement : https://leetcode.com/problems/reverse-nodes-in-k-group/
    Link for solution understanding : https://www.techiedelight.com/reverse-every-k-nodes-of-a-linked-list/
    """
    # base case
    if head is None:
        return None

    # start with the current node
    current = head

    # reverse next `k` nodes
    prev = None
    count = 0

    # iterate through the list and move/insert each node
    # in front of the result list (like a push of the node)
    while current and count < k:
        count = count + 1

        # tricky: note the next node
        next = current.next

        # move the current node onto the result
        current.next = prev

        # update the previous pointer to the current node
        prev = current

        # move to the next node in the list
        current = next

    # recur for remaining nodes
    head.next = reverseInGroups(current, k)

    # it is important to return the previous node (to link every group of `k` nodes)
    return prev


if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    head = reverseInGroups(head, 2)
    head.print()
