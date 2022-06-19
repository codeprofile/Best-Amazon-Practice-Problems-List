from implementation_singly_LinkedList import Node, LinkedList
from typing import Optional

class Solution:
    """
    Problem statement : https://leetcode.com/problems/merge-two-sorted-lists/
    Solution understanding video link : https://www.youtube.com/playlist?list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo
    """
    def mergeTwoLists(self, list1: Optional[LinkedList], list2: Optional[LinkedList]) -> Optional[Node]:
        currentFirst = list1.head
        currentSecond = list2.head
        mergedList = LinkedList()
        while True:
            if currentFirst is None:
                mergedList.insertEnd(currentSecond)
                break
            if currentSecond is None:
                mergedList.insertEnd(currentFirst)
                break
            if currentFirst.data < currentSecond.data:
                currentFirstNext = currentFirst.next
                currentFirst.next = None
                mergedList.insertEnd(currentFirst)
                currentFirst = currentFirstNext
            else:
                currentSecondNext = currentSecond.next
                currentSecond.next = None
                mergedList.insertEnd(currentSecond)
                currentSecond = currentSecondNext
        return mergedList.printList()


if __name__ == "__main__":
    # Construct First Linked List
    nodeOne = Node(1)
    nodeTwo = Node(3)
    nodeThree = Node(4)
    firstList = LinkedList()
    firstList.insertEnd(nodeOne)
    firstList.insertEnd(nodeTwo)
    firstList.insertEnd(nodeThree)

    # Construct Second List
    nodeFour = Node(2)
    nodeFive = Node(7)
    nodeSix = Node(9)
    secondList = LinkedList()
    secondList.insertEnd(nodeFour)
    secondList.insertEnd(nodeFive)
    secondList.insertEnd(nodeSix)
    print("Printing first list")
    print(firstList.printList())
    print("Printing second list")
    print(secondList.printList())

    print(Solution().mergeTwoLists(firstList, secondList))
