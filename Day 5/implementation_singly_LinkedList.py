class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    If we are new to Linked list follow below youtube playlist:
    understanding video link : https://www.youtube.com/playlist?list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo
    """

    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def deleteAt(self, position: int):
        """
        Delete A Node In Between Two Nodes
        Program Logic
        >> Traverse till the node which you want to delete
        >> Preserve the details of the previous node
        >> Establish a connection from the next of the previous node
        to the next of this node
        >> Make the next of this node point to None
        """
        if position < 0 or position > self.listLength():
            print(f"Entered Position {position} is invalid")
            return
        if position == 0:
            self.head = self.head.next
            return
        currentNode = self.head
        nodecount = 0
        while True:
            if nodecount == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            nodecount += 1

    def deleteEnd(self):
        """
            Delete A Node From The End of The List
            Program Logic
            >> Traverse till the end of the list
            >> Preserve the  second last node in a temporary node
            >> Delete the last node
            >> Make the next of the temporary node point to None
        """
        currentNode = self.head
        while True:
            if currentNode.next is None:
                previousNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next

    def insertHead(self, newNode):
        """
           Insert A New Node As The Head Node
           Program Logic :
           >> Preserve the current head node in temporary node
           >> Make the new node as the head node
           >> Make the next of your new node point to the temporary node
        """
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self, newNode, position: int):
        """
            Insert A New Node In Between Two Nodes
            Program Logic
            >> Traverse the list till position 1
            >> Store the details of previous node
            >> Make a connection from the next of previous node to new node
            >> Make a connection from next of new node to node at position 1
            >> The new node now becomes your node ar position 1 and the node that was
            earlier at position 1 now becomes the node at position2
        """
        if position < 0 or position > self.listLength():
            print(f"Entered Position {position} is invalid")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentposition = 0
        while True:
            if currentposition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentposition += 1

    def insertEnd(self, newNode):
        # If head is None then it's the empty linked list
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next

    def printList(self):
        currentNode = self.head
        nodelist = []
        while True:
            nodelist.append(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        return nodelist


if __name__ == "__main__":
    firstNode = Node("Laxmi")
    linkedList = LinkedList()
    linkedList.insertEnd(firstNode)
    secondNode = Node("Sarki")
    linkedList.insertEnd(secondNode)
    thirdNode = Node("Is")
    linkedList.insertHead(thirdNode)
    fourthnode = Node("My")
    linkedList.insertAt(fourthnode, 1)
    fifthnode = Node("Name")
    linkedList.insertAt(fifthnode, 2)
    linkedList.deleteEnd()
    linkedList.deleteAt(3)
    linkedList.print()
