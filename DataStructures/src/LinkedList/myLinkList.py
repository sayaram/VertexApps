from LinkedList import Node


class myLinkList:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            looped = self.head
            while looped.next is not None:
                looped = looped.next
            looped.next = new_node

    def find2ndLast(self):
        looped = self.head
        if self.head.next is None:
            return None
        else:
            while looped.next.next is not None:
                looped = looped.next
            return looped.data

    def findMiddle(self):
        looped = self.head
        fast = self.head
        if self.head.next.next is None:
            return None
        else:
            while fast.next is not None:
                fast = fast.next.next
                looped = looped.next
            return looped.data


if __name__ == '__main__':
    objList = myLinkList()
    objList.add(4)
    objList.add(8)
    objList.add(12)
    objList.add(16)
    objList.add(20)
    print(objList.find2ndLast())
    print(objList.findMiddle())
