class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        return curr.val if curr and index == 0 else -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def remove(self, index: int) -> bool:
        prev = None
        curr = self.head
        idx = 0
        while idx < index and curr:
            prev = curr
            curr = curr.next
            idx += 1
        if not curr:
            return False
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
