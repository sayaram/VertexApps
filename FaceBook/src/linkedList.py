class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def list_print(self):
        printable = self.head
        while printable is not None:
            print(printable.data)
            printable = printable.next

    def find_nth(self, item):
        printable = self.head
        size = 1
        while printable is not None:
            if size < item:
                printable = printable.next
            elif size == item:
                return printable
            size = size + 1
        return None

    def find_secondlast(self):
        temp = self.head
        if temp is None or temp.next is None:
            return -1
        while temp is not None:
            if temp.next.next is None:
                return temp.data
            temp = temp.next

    def find_middle(self):
        fast = self.head
        slow = self.head
        if fast is None or fast.next is None:
            return -1
        while fast is not None:
            if fast.next is None:
                return slow.data
            fast = fast.next.next
            slow = slow.next
        return -1


if __name__ == '__main__':
    link = LinkedList()
    link.add_item(4)
    link.add_item(9)
    link.add_item(10)
    link.add_item(20)
    link.add_item(18)
    print(link.find_nth(2).data)
    link.list_print()
    print(link.find_secondlast)
    print(link.find_middle)
