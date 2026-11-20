class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1

        return -1 

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

            return

        newNode.next = self.head
        self.head = newNode


    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode

            return

        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        prev = self.head

        count = 0
        while curr:
            if index == 0:
                self.head = curr.next
                return True

            if index == count:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True

            prev = curr
            curr = curr.next
            count += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
