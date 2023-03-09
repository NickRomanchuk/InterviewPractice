class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, head=None):
        self.head = head
    
    def print(self):

        current = self.head
        while current:
            print(current.value, '->', end='')
            current = current.next
        
        print(' None')

def main():

    llist = LinkedList()
    llist.print()

    e1 = Node(1)
    llist = LinkedList(e1)
    llist.print()

main()
