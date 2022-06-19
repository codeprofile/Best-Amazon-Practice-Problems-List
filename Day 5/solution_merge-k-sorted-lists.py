class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    """
    Problem statement : https://leetcode.com/problems/merge-k-sorted-lists/
    Understanding solution : https://www.techiedelight.com/efficiently-merge-k-sorted-linked-lists/
    Here we have solved this using Divide Conquer technique
    The time complexity of the above solution is O(n.log(k))
    as the outer while loop in function mergeKLists() runs O(log(k)) times, and every time we are processing n nodes.
    """

    def printList(self, node):
        """ utility function to print content of a linked List """
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    def sortedMerge(self, a, b):
        """ Takes 2 lists sorted in increasing order and merges their nodes
            to make one sorted list
        """

        # base cases
        if a is None:
            return b
        if b is None:
            return a

        # Pick either `a` or `b` and recur
        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergekLists(self,lists):
        """
        :param lists:
        :return: generates a single sorted linked list
        """

        # base case
        if not lists:
            return None

        last = len(lists) -1

        # repeat until only one list is left
        while last:
            (i,j) = (0,last)

            # `(i,j)` forms a pair
            while i < j:
                # merge list `j` with `i`
                lists[i] = self.sortedMerge(lists[i],lists[j])

                # consider the next pair
                i = i + 1
                j = j - 1

                # if all pairs are merged , update last
                if i >= j:
                    last = j

        return lists[0]


if __name__ == "__main__":
    k = 3 # total number of linked lists

    # a list  to store the head nodes of the linked lists
    lists = [Node] * k

    lists[0] = Node(1)
    lists[0].next = Node(5)
    lists[0].next.next = Node(7)

    lists[1] = Node(2)
    lists[1].next = Node(3)
    lists[1].next.next = Node(6)
    lists[1].next.next.next = Node(9)

    lists[2] = Node(4)
    lists[2].next = Node(8)
    lists[2].next.next = Node(10)

    # Merge all lists into one
    head = Solution().mergekLists(lists)
    Solution().printList(head)
