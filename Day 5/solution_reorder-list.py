from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    problem statement : https://leetcode.com/problems/reorder-list/
    understanding solution link : https://www.goodtecher.com/leetcode-143-reorder-list/
    Find the first half and second half of the node list.
    Keep the first half order, and reverse the second half node list.
    Then mix the nodes from the first half list and the second half list.
    """
    def printList(self, head):
        while head != None:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0

        current = head

        while current != None:
            current = current.next
            count += 1

        if count % 2 == 0:
            mid = count // 2
        else:
            mid = (count + 1) // 2

        first_half = []
        second_half = []

        current = head
        index = 0

        while current != None:
            if index < mid:
                first_half.append(current)
            else:
                second_half.append(current)

            current = current.next
            index += 1

        second_half = list(reversed(second_half))

        current = first_half.pop(0)
        current_head = current

        for i in range(count - 1):
            if i % 2 == 0:
                current.next = second_half.pop(0)
            else:
                current.next = first_half.pop(0)

            current = current.next

        current.next = None
        self.printList(current_head)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    Solution().reorderList(head)
